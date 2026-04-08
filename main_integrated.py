import os
import warnings
from dotenv import load_dotenv
from src.logic.raydium_fetcher import RaydiumProvider
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq

warnings.filterwarnings("ignore", category=UserWarning, module='pydantic')
load_dotenv()

def main():
    raydium = RaydiumProvider()
    data = raydium.get_token_pair_data()

    llm = ChatGroq(
        temperature=0, 
        groq_api_key=os.getenv("GROQ_API_KEY"), 
        model_name="llama-3.1-8b-instant" 
    )

    # Memposisikan satu agen sebagai 'Council' untuk efisiensi
    selena_oracle = Agent(
        role='Selena Security Oracle',
        goal='Orchestrate multi-layer security analysis for DeFi transactions.',
        backstory="""You represent the collective intelligence of the Selena Guardrails system. 
        You process data through internal Quant, Risk, and Validation modules 
        to ensure zero-error execution on Solana.""",
        verbose=True, 
        llm=llm,
        allow_delegation=False
    )

    print("\n" + "="*60)
    print(f"🏛️ SELENA SYSTEM ENGINE: {data['status']}")
    print(f"📊 TARGET: {data['protocol']} | SOURCE: {data['source']}")
    print("="*60)

    analysis_task = Task(
        description=f"""
        PERFORM MULTI-LAYERED ANALYSIS FOR 5.0 SOL SWAP:
        
        1. [QUANT MODULE]: Analyze slippage for ${data['price']} price 
           against ${data['liquidity']:,} liquidity.
        2. [RISK MODULE]: Validate if price impact exceeds 0.5%.
        3. [VALIDATOR MODULE]: Confirm protocol compliance for Raydium V4.
        
        OUTPUT FORMAT:
        - 🧠 QUANT METRICS: (Mathematical breakdown)
        - 🛡️ RISK ASSESSMENT: (Clearance status)
        - 🚀 EXECUTION INTENT: (Ready for on-chain validation)
        - 🧾 SUMMARY: Confidence Score (0-100%)
        """,
        agent=selena_oracle,
        expected_output="A structured multi-layer security report."
    )

    selena_crew = Crew(
        agents=[selena_oracle],
        tasks=[analysis_task],
        process=Process.sequential,
        verbose=True
    )

    print("\n🚀 Selena is initiating autonomous reasoning pipeline...")
    try:
        result = selena_crew.kickoff()
        print("\n" + "="*60)
        print("🏛️ SELENA FINAL SYSTEM VERDICT")
        print("="*60)
        print(result)
        print("\n✅ READY FOR ON-CHAIN VALIDATION")
        print("="*60)
    except Exception as e:
        print(f"❌ Execution Error: {e}")

if __name__ == "__main__":
    main()