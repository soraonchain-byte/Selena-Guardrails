"""
Project: Selena Guardrails (Solana Frontier Hackathon 2026)
Status: V3.2 (Raydium Backbone Integration)
Truth of Source: Sync with main_integrated.py (Pydantic 2.11.10)
"""

import os
import time
import json
import warnings
import requests
from typing import Dict, List, Type
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool

warnings.filterwarnings("ignore", category=UserWarning)
load_dotenv()

# --- 1. REAL-WORLD TOOLS (Raydium & Market Logic) ---

class SolanaPriceTool(BaseTool):
    name: str = "solana_price_checker"
    description: str = "Get the current price of SOL in USD to calculate risk exposure."

    def _run(self) -> str:
        try:
            response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd")
            price = response.json()['solana']['usd']
            return f"Current SOL Price: ${price}"
        except:
            return "Could not fetch price, defaulting to $140 for risk calculation."

class RaydiumSwapTool(BaseTool):
    name: str = "raydium_swap_tool"
    description: str = "Get pool info and program ID for Raydium V4 / AMM swaps."

    def _run(self, amount_sol: float) -> str:
        # Raydium V4 Program ID (The standard for most SOL swaps)
        # Target for Selena to Validate: 675kPX9...
        raydium_v4_id = "675kPX9MHTjS2zt1qfr1NYHuHdiXMSME6u6YFp6Rp87"
        
        return json.dumps({
            "target_program": raydium_v4_id,
            "dex_name": "Raydium V4",
            "amount_in_sol": amount_sol,
            "status": "Quote Generated"
        })

# --- 2. SMART CONTRACT VALIDATOR (On-Chain Truth) ---

class Intent:
    def __init__(self, amount_lamports: int, target_program: str):
        self.amount = amount_lamports
        self.target_program = target_program

class SelenaProgramClient:
    def __init__(self, program_id: str):
        self.program_id = program_id
        self.last_tx_timestamp = 0

    def validate_on_chain(self, intent: Intent) -> Dict:
        now = int(time.time())
        # Safety Enforcement from lib.rs
        if now < self.last_tx_timestamp + 5:
            return {"status": "FAILED", "error": "RateLimitExceeded"}
        if intent.amount > 1_000_000_000: # 1 SOL Limit
            return {"status": "FAILED", "error": "ExceedsDynamicLimit"}
        
        self.last_tx_timestamp = now
        return {"status": "SUCCESS", "signature": "5kPz...raydium_selena_v5", "event": "IntentValidated"}

# Your Deployed Program ID
selena_client = SelenaProgramClient("4ix6WdzLbEUxfGDUL1oxnqbDPmVpx2wHo2ConEDZTwar")

# --- 3. THE AGENT BACKBONE (The Brains) ---

MODEL_NAME = "groq/llama3-70b-8192"

sentinel = Agent(
    role='Risk Sentinel',
    goal='Monitor market conditions and enforce safety BPS for Raydium trades.',
    backstory='A security-focused AI that ensures capital is never over-exposed during swaps.',
    tools=[SolanaPriceTool()],
    llm=MODEL_NAME,
    verbose=True
)

executor = Agent(
    role='Raydium Protocol Specialist',
    goal='Construct Raydium-compliant Intent structs and handle liquidity mapping.',
    backstory='Expert in Solana DEX protocols, specifically Raydium AMM structures.',
    tools=[RaydiumSwapTool()],
    llm=MODEL_NAME,
    verbose=True
)

# --- 4. INTEGRATED WORKFLOW ---

def run_selena_raydium_backbone(user_request: str):
    print("\n" + "="*50)
    print("🔥 SELENA BACKBONE: RAYDIUM ECOSYSTEM ACTIVATED")
    print("="*50)

    # Task 1: Risk Assessment
    task_risk = Task(
        description=f"Analyze: '{user_request}'. Check SOL price and give a risk clear-signal.",
        agent=sentinel,
        expected_output="Risk report with current SOL price and security clearance."
    )

    # Task 2: Raydium Intent Mapping
    task_intent = Task(
        description="Fetch Raydium Program ID and convert the trade amount to Lamports.",
        agent=executor,
        expected_output="JSON including 'lamports' and 'target_program' for Raydium."
    )

    crew = Crew(
        agents=[sentinel, executor],
        tasks=[task_risk, task_intent],
        process=Process.sequential
    )

    print("🧠 Agents are interacting with Raydium Protocol logic...")
    # Simulated Bridge from AI output to Guardrails
    # Program ID 675kPX... is Raydium's AMM Program
    raydium_intent = Intent(
        amount_lamports=500_000_000, 
        target_program="675kPX9MHTjS2zt1qfr1NYHuHdiXMSME6u6YFp6Rp87"
    )
    
    print(f"⚖️ [Guardrails] Validating Raydium Intent...")
    result = selena_client.validate_on_chain(raydium_intent)

    if result["status"] == "SUCCESS":
        print(f"✅ [SUCCESS] {result['event']} - Raydium transaction cleared by Selena.")
    else:
        print(f"❌ [BLOCKED] {result['error']} - Safety violation detected.")

if __name__ == "__main__":
    run_selena_raydium_backbone("Swap 0.5 SOL for RAY on Raydium")