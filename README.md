# LemonadeBench
🍋 A lightweight performance profiling and benchmarking suite for local AI inference using AMD Lemonade. Measures TTFT, TPS, and generates visual analytics.


# 🍋 LemonadeBench: The Local AI Profiling Suite

![Status](https://img.shields.io/badge/Status-Active_Development-yellow)
![Platform](https://img.shields.io/badge/Platform-AMD_Lemonade-blue)
![Focus](https://img.shields.io/badge/Focus-Performance_Eval-red)

## 📌 What is LemonadeBench?
**LemonadeBench** is an open-source performance evaluation tool built specifically for the **AMD Lemonade** ecosystem. 

As local AI becomes more prevalent, developers need robust, easy-to-use tools to measure hardware efficiency, bottleneck identification, and token generation speeds. LemonadeBench connects directly to the local Lemonade API to run automated stress tests and generate comparative visual analytics.

## 🎯 Key Features (In Development)
- **⏱️ TTFT Measurement:** Accurate tracking of *Time To First Token*.
- **🚀 TPS Profiling:** Real-time *Tokens Per Second* calculation under varying context lengths.
- **📊 Visual Analytics:** Automated generation of Matplotlib/Seaborn bar charts comparing different quantizations (e.g., INT4 vs FP16).
- **💻 Graceful Degradation Testing:** Proving how Lemonade performs on legacy hardware vs. modern NPUs.

## 📖 The Story & Motivation (AMD Lemonade Challenge)
I am an AI Systems engineering student who usually benchmarks Datacenter GPUs (recently writing custom FP8 Triton Kernels for B200 architectures). However, my personal local machine is a **4-year-old Lenovo IdeaPad with a broken screen and a failing keyboard**. 

I started building LemonadeBench to evaluate how well AMD Lemonade optimizes models on heavily constrained, legacy hardware. **The goal?** To prove that Lemonade is highly accessible. 

**Why I need the AMD Ryzen™ AI Max+ 395 laptop:**
While building this tool on my legacy hardware proves Lemonade's excellent fallback capabilities, my ultimate goal is to profile **Strix Halo NPUs and iGPU hybrid acceleration natively**. Winning the Lemonade Developer Challenge would provide the exact hardware needed to evolve this project from a basic API profiler into a full-fledged NPU/iGPU benchmarking suite.

## 🛠️ Current Status
- [x] Architecture design and metrics definition.
- [ ] AMD Lemonade Local API integration (Ongoing).
- [ ] Visualization engine implementation.

*Code drops are incoming over the next 48-72 hours!*
