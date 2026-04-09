<img width="5008" height="952" alt="Banner-Sora" src="https://github.com/user-attachments/assets/35a2d602-aa7c-4563-891a-4a9b2c6b351b" />

---
# 🛡️ Selena Guardrails: Multi-Agent Security Layer for Solana
<img width="3894" height="703" alt="Selena_logo_banner" src="https://github.com/user-attachments/assets/253074ea-a5ad-45f1-accd-eb81a89ffa38" />

Selena is an **Autonomous Security Oracle** designed to protect the Agentic Economy on Solana. It acts as a high-fidelity validation layer that bridges off-chain AI reasoning with on-chain financial safety, specifically optimized for the Raydium Protocol.

## 🏛️ The Problem & Vision
In the emerging **Agentic Economy**, autonomous AI agents manage capital. However, these agents often lack real-time risk awareness, making them vulnerable to slippage, sandwich attacks, and liquidity traps. 

**Selena** solves this by providing a **Multi-Layered Guardrail System** that intercept AI intents, performs deep-tier risk analysis, and issues security clearances before any transaction touches the blockchain.

## ✨ Key Features
- **Multi-Agent Consensus Pipeline**: Uses specialized AI agents (Quant, Risk, and Validator) to audit transactions.
- **Dynamic Slippage Oracle**: Real-time calculation of price impact vs pool depth.
- **Resilient Data Intelligence**: Features a **Verified Simulation Layer** to maintain security auditing even during network congestion or API rate-limiting.
- **Raydium V4 Optimization**: Specialized logic for Solana's most liquid AMM pools.

## 🧠 Multi-Agent Architecture
Selena operates through an orchestration of specialized modules:
1. **Selena Quant Engine**: Mathematically analyzes pool dynamics and slippage.
2. **Selena Risk Sentinel**: Evaluates intents against strict security boundaries.
3. **Selena Execution Router**: Formulates the final verdict and prepares the transaction intent for on-chain validation.

## 🛠️ Tech Stack
- **AI Orchestration**: CrewAI (Multi-Agent Framework)
- **Inference Engine**: Groq (Llama 3.1 8B)
- **Blockchain Focus**: Solana (Raydium V4 AMM)
- **Language**: Python 3.11.9 (Core Logic), Rust/Anchor (On-chain Blueprint)

## 🚦 System Status & Demo
When running the engine, Selena performs a phased audit:
- **Status: LIVE_VERIFIED** (Real-time Market Sync)
- **Status: STRESS_TEST_MODE** (Internal Verified Simulation)

### Example Output
```text
🧠 QUANT METRICS: Slippage 0.00033% | Price Impact 0.05%
🛡️ RISK ASSESSMENT: CLEARED
🚀 EXECUTION INTENT: COMPLIANT & READY
🧾 SUMMARY: Confidence Score 99.99%

---

💻 Installation & Setup
Clone the repository:

git clone [https://github.com/soraonchain-byte/Selena-Guardrails.git](https://github.com/soraonchain-byte/Selena-Guardrails.git)
cd Selena-Guardrails
Environment Setup:
Create a .env file and add your credentials:

# Selena Guardrails - API Configuration
# Get your key from: https://console.groq.com/keys
GROQ_API_KEY=gsk_your_key_here_xxxx

# Optional: If you use OpenAI in the future
OPENAI_API_KEY=your_openai_key_here

Run the Guardrails Engine:

python main_integrated.py

---
Built for the Solana Frontier Hackathon 2026 by Sora Onchain.
