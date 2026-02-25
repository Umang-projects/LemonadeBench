import time
import requests
import csv
import argparse
import random
import matplotlib.pyplot as plt

# ==========================================
# LemonadeBench: The Local AI Profiling Suite
# ==========================================

class LemonadeBench:
    def __init__(self, api_url="http://localhost:8000/v1/completions", model_name="lemonade-local", mock=False):
        self.api_url = api_url
        self.model_name = model_name
        self.mock = mock
        self.results = []

    def run_benchmark(self, prompt, max_tokens=100, run_id=1):
        print(f"\n[Run {run_id}] 🚀 Profiling Prompt: '{prompt[:30]}...'")
        
        # === MOCK MODE (For Testing without Server) ===
        if self.mock:
            time.sleep(1) # Simulate network delay
            ttft = random.uniform(20.0, 50.0) # Fake TTFT between 20-50ms
            tps = random.uniform(15.0, 35.0)  # Fake TPS between 15-35 tokens/sec
            total_time = (max_tokens / tps) + (ttft / 1000)
            print(f"✅ [MOCK MODE] TTFT: {ttft:.2f} ms | TPS: {tps:.2f} tokens/sec")
            
            self.results.append({
                "run_id": run_id, "prompt_length": len(prompt),
                "ttft_ms": round(ttft, 2), "tps": round(tps, 2), "total_time_s": round(total_time, 2)
            })
            return

        # === REAL API CALL MODE ===
        payload = {"model": self.model_name, "prompt": prompt, "max_tokens": max_tokens, "stream": True}
        start_time = time.time()
        first_token_time = None
        token_count = 0
        
        try:
            response = requests.post(self.api_url, json=payload, stream=True, timeout=5)
            for line in response.iter_lines():
                if line:
                    if first_token_time is None:
                        first_token_time = time.time()
                    token_count += 1
            end_time = time.time()
            
            ttft = (first_token_time - start_time) * 1000 if first_token_time else 0
            total_time = end_time - start_time
            tps = token_count / total_time if total_time > 0 else 0
            
            print(f"✅ TTFT: {ttft:.2f} ms | TPS: {tps:.2f} tokens/sec")
            self.results.append({
                "run_id": run_id, "prompt_length": len(prompt),
                "ttft_ms": ttft, "tps": tps, "total_time_s": total_time
            })
            
        except requests.exceptions.RequestException:
            print(f"❌ [Error] Lemonade server not found at {self.api_url}.")

    def export_to_csv(self, filename="lemonade_benchmark_results.csv"):
        if not self.results: return
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.results[0].keys())
            writer.writeheader()
            writer.writerows(self.results)
        print(f"💾 Results exported to {filename}")

    def generate_graphs(self, filename="example_performance_graph.png"):
        if not self.results: return
        
        runs = [r["run_id"] for r in self.results]
        ttft_data = [r["ttft_ms"] for r in self.results]
        tps_data = [r["tps"] for r in self.results]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        ax1.bar(runs, ttft_data, color='orange')
        ax1.set_title('Time To First Token (TTFT)')
        ax1.set_xlabel('Run ID'); ax1.set_ylabel('TTFT (ms)')

        ax2.plot(runs, tps_data, marker='o', color='green', linewidth=2)
        ax2.set_title('Tokens Per Second (TPS)')
        ax2.set_xlabel('Run ID'); ax2.set_ylabel('TPS')

        plt.tight_layout()
        plt.savefig(filename)
        print(f"📈 Visualization saved as {filename}")

def main():
    parser = argparse.ArgumentParser(description="LemonadeBench: AMD Local AI Profiler")
    parser.add_argument("--url", default="http://localhost:8000/v1/completions", help="API Endpoint")
    parser.add_argument("--runs", type=int, default=5, help="Number of benchmark iterations")
    parser.add_argument("--mock", action="store_true", help="Run in mock mode without server")
    args = parser.parse_args()

    print("=========================================")
    print("🍋 LemonadeBench Performance Suite Init")
    print("=========================================")

    bench = LemonadeBench(api_url=args.url, mock=args.mock)

    prompts = [
        "Explain quantum computing in simple terms.",
        "Write a Python script to scrape a website.",
        "What are the benefits of AMD NPU architecture?",
        "Summarize the history of artificial intelligence.",
        "Draft an email to my boss asking for a laptop upgrade."
    ]

    for i in range(min(args.runs, len(prompts))):
        bench.run_benchmark(prompt=prompts[i], run_id=i+1)

    bench.export_to_csv()
    bench.generate_graphs()

if __name__ == "__main__":
    main()