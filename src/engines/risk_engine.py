"""
Module: risk_engine.py
Standard: Rule-based verification for Guardrails
"""

class RiskEngine:
    def __init__(self, max_price_impact=0.5):
        self.max_price_impact = max_price_impact

    def evaluate_risk(self, quant_data: dict) -> dict:
        if quant_data.get("status") != "SUCCESS":
            return {"risk_level": "CRITICAL", "verdict": "REJECTED", "reason": "Quant Analysis Failed"}

        price_impact = quant_data.get("price_impact_percent", 100)
        
        if price_impact > self.max_price_impact:
            return {
                "risk_level": "HIGH",
                "verdict": "REJECTED",
                "reason": f"Price impact {price_impact}% exceeds threshold {self.max_price_impact}%"
            }
        
        return {
            "risk_level": "LOW",
            "verdict": "CLEARED",
            "reason": "All safety boundaries respected."
        }