"""
Project: Selena Guardrails (Solana Frontier 2026)
Role: Off-chain Multi-Agent Council Orchestration
Description: Defines the 4 specialized agents for financial governance consensus using Groq for high-speed inference.
"""

import os
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SelenaCouncil:
    def __init__(self):
        # Using Groq Llama-3-70b for high-speed reasoning without taxing local CPU
        self.llm = ChatGroq(
            temperature=0.2,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama3-70b-8192"
        )

    def define_agents(self):
        """
        Define 4 core agents with specialized personas for the Council.
        """
        
        # 1. Oracle: Grounding agent for market data
        self.oracle = Agent(
            role='Market Data Oracle',
            goal='Validate on-chain data accuracy and identify real-world market conditions.',
            backstory='Expert in Solana cluster analysis. Prevents the system from hallucinating based on stale price data.',
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

        # 2. Quant: Strategic proposal generator
        self.quant = Agent(
            role='Quantitative Strategist',
            goal='Propose high-value treasury rebalancing or trade intents based on risk-adjusted returns.',
            backstory='DeFi math genius. Focuses on capital efficiency while respecting volatility bounds.',
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

        # 3. Validator: Adversarial auditor
        self.validator = Agent(
            role='Adversarial Risk Auditor',
            goal='Identify potential failure points, MEV risks, or vulnerabilities in the Quant proposal.',
            backstory='The ultimate Devil Advocate. If there is a way to lose money, this agent will find it.',
            llm=self.llm,
            verbose=True,
            allow_delegation=True
        )

        # 4. Sentinel: Risk alignment and governance reporting
        self.sentinel = Agent(
            role='Treasury Sentinel',
            goal='Ensure all intents comply with the global Investment Policy Statement (IPS) and BPS limits.',
            backstory='The guardian of the treasury. Has final authority to block or approve the Council’s decision.',
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

    def run_governance_process(self, intent_data):
        """
        Orchestrate the council to review a specific trade/rebalance intent.
        """
        self.define_agents()

        # Task definition for the entire Council
        governance_task = Task(
            description=(
                f"Review this intent: {intent_data}. "
                "The Oracle must verify liquidity, the Quant must justify the logic, "
                "the Validator must find risks, and the Sentinel must provide the final verdict."
            ),
            expected_output="A structured report: [STATUS: APPROVED/REJECTED] followed by a 3-point reasoning summary.",
            agent=self.sentinel
        )

        # Create sequential crew for high-value audit trail
        selena_crew = Crew(
            agents=[self.oracle, self.quant, self.validator, self.sentinel],
            tasks=[governance_task],
            process=Process.sequential,
            verbose=True
        )
        
        return selena_crew.kickoff()