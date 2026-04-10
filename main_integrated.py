import os
import time
import json
import warnings
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq

# Import Custom Frameworks & Engines
from src.logic.raydium_fetcher import RaydiumProvider
from src.logic.sora_pulse import SoraPulse
from src.engines.quant_engine import QuantEngine
from src.engines.risk_engine import RiskEngine

warnings.filterwarnings("ignore", category=UserWarning, module='pydantic')
load_dotenv()

def main():
    # 1. Initialize Components
    orchestrator = SoraPulse()
    raydium = RaydiumProvider()
    quant = QuantEngine(target_slippage_bps=50) # 0.5%
    risk = RiskEngine(max_price_impact=0.5)
    
    # 2. Setup LLM (For Explanation only, not Math)
    llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-8b-instant")

    # 3. Data Fetching
    market_data = raydium.get_token_pair_data()
    orchestrator.emit_pulse("SELENA_ORACLE", 1, "MARKET_SYNC_COMPLETE")

    # 4. DETERMINISTIC PIPELINE (Pure Python)
    print("\n⚙️ [ENGINE] Running Deterministic Calculations...")
    quant_results = quant.calculate_trade_metrics(5.0, market_data['price'], market_data['liquidity'])
    risk_results = risk.evaluate_risk(quant_results)
    
    # 5. AGENTIC REASONING (Narrative Layer)
    if orchestrator.sync_reaction("SELENA_ORACLE", 1):
        orchestrator.emit_pulse("SELENA_ORACLE", 2, "RUNNING_NARRATIVE_AUDIT")
        
        selena_oracle = Agent(
            role='Selena Security Oracle',
            goal='Explain technical security audits in human-readable intents.',
            backstory="You are a validator that translates JSON engine data into security clearances.",
            llm=llm,
            allow_delegation=False
        )

        analysis_task = Task(
            description=f"""
            TRANSCRIPT AUDIT:
            Quant Data: {json.dumps(quant_results)}
            Risk Data: {json.dumps(risk_results)}
            
            Instruction: Explain the math provided above. Do not calculate yourself. 
            Confirm if the status is CLEARED or REJECTED.
            """,
            agent=selena_oracle,
            expected_output="A structured security clearance report based on engine data."
        )

        crew = Crew(agents=[selena_oracle], tasks=[analysis_task], verbose=True)
        final_report = crew.kickoff()
        
        print("\n" + "="*60)
        print(final_report)
        print("="*60)
        orchestrator.emit_pulse("SELENA_ORACLE", 3, "AUDIT_COMPLETE")

if __name__ == "__main__":
    main()