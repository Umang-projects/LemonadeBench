# LemonadeBench
🍋 A lightweight performance profiling and benchmarking suite for local AI inference using AMD Lemonade. Measures TTFT, TPS, and generates visual analytics.

# 🍋 LemonadeBench: The Local AI Profiling Suite

![Status](https://img.shields.io/badge/Status-Active_Development-green)
![Platform](https://img.shields.io/badge/Platform-AMD_Lemonade-blue)
![License](https://img.shields.io/badge/License-Open_Source-orange)

## 📌 What is LemonadeBench?
**LemonadeBench** is an open-source performance evaluation and benchmarking client built specifically for the **AMD Lemonade** local AI ecosystem. 

As developers shift towards running LLMs locally, measuring hardware efficiency becomes critical. LemonadeBench connects directly to the local Lemonade API (OpenAI-compatible) to run automated stress tests and generate visual analytics.

## 🎯 Key Features
- **⏱️ TTFT Measurement:** Accurate tracking of *Time To First Token* (crucial for perceived latency).
- **🚀 TPS Profiling:** Real-time *Tokens Per Second* calculation under varying context lengths.
- **📊 Visual Analytics:** Automated generation of Matplotlib bar and line charts to visualize performance across multiple runs.
- **💾 CSV Export:** Automatically logs benchmark metrics for further analysis.

## 📖 The Story (AMD Lemonade Challenge)
I am an AI Systems engineering student who usually benchmarks Datacenter GPUs (recently wrote custom FP8 Triton Kernels for NVIDIA B200). However, my personal local machine is a old Lenovo IdeaPad. 

I built LemonadeBench to evaluate how well AMD Lemonade optimizes models. Since my current hardware struggles to natively host large LLMs, I engineered a robust `--mock` mode to test the profiling, CSV export, and graphing pipeline without needing a live server. 

**My Goal:** Winning the **AMD Ryzen™ AI Max+ 395 laptop** will allow me to run this benchmarking suite natively against real local models, extending it to profile Strix Halo NPUs and iGPU hybrid acceleration properly!

## 🛠️ How to Run

### 1. Installation
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/LemonadeBench.git
cd LemonadeBench
pip install -r requirements.txt

## 🛠️ Current Status
- [x] Architecture design and metrics definition.
- [ ] AMD Lemonade Local API integration (Ongoing).
- [ ] Visualization engine implementation.

*Code drops are incoming over the next 48-72 hours!*
