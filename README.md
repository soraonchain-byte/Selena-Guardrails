# 🛡️ Selena Guardrails: Secure Agentic Economy on Solana

Selena is an autonomous security validation layer designed for AI Agents operating on the Solana blockchain. It bridges the gap between off-chain AI reasoning and on-chain financial safety.

## 🚀 The Vision
In the **Agentic Economy**, AI agents act as capital managers. However, without proper guardrails, these agents are vulnerable to logic errors, slippage attacks, and unauthorized drainage. Selena provides a **non-custodial validation layer** that ensures every AI intent remains within pre-defined safety parameters.

## ✨ Key Features
- **Raydium V4 Integration**: Specialized validation for liquidity-intensive swaps on Raydium.
- **Dynamic Risk Scaling**: Automatically calculates risk BPS based on real-time market data.
- **Rate Limiting Enforcement**: Prevents high-frequency trading anomalies at the smart contract level.
- **Autonomous Backbone**: Powered by CrewAI agents (Sentinel & Executor) using the LiteLLM bridge.

## 🛠️ Architecture
1. **The Sentinel (AI)**: Analyzes market volatility and defines safety thresholds.
2. **The Executor (AI)**: Maps natural language intents into technical blockchain instructions.
3. **Selena Guardrails (Program)**: The final on-chain judge that validates instructions against the `Intent` struct before execution.

## 💻 Tech Stack
- **Languages**: Rust (Anchor), Python (Backbone)
- **Frameworks**: CrewAI, LiteLLM
- **DEX Focus**: Raydium V4

## 🚦 Quick Start
1. Clone the repository:
   ```bash
   git clone [https://github.com/soraonchain-byte/Selena-Guardrails.git](https://github.com/soraonchain-byte/Selena-Guardrails.git)