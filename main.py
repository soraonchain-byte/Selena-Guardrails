"""
Project: Selena Guardrails (Solana Frontier 2026)
Entry Point: Main execution script for the local demo.
"""

from agents.council import SelenaCouncil
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("--- 🛡️ SELENA GUARDRAILS ACTIVE ---")
    
    # Initialize the Council
    council = SelenaCouncil()
    
    # Example Intent: A high-value trade proposal
    # Narrative: AI wants to move 50,000 USD to a Staking Vault.
    intent_data = {
        "action": "DEPOSIT",
        "asset": "SOL",
        "amount": 50000,
        "target": "Solana_Staking_Vault",
        "reason": "Optimize yield during low volatility period."
    }

    print(f"\n[System] New Intent Received: {intent_data['action']} {intent_data['amount']} {intent_data['asset']}")
    
    # Run the Multi-Agent Council Reasoning
    try:
        final_report = council.run_governance_process(intent_data)
        
        print("\n" + "="*50)
        print("🏛️ FINAL COUNCIL REPORT")
        print("="*50)
        print(final_report)
        
    except Exception as e:
        print(f"❌ Error during execution: {e}")
        print("Ensure your GROQ_API_KEY is set in the .env file.")

if __name__ == "__main__":
    main()