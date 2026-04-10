"""
Module: quant_engine.py
Standard: Pure Python Deterministic Math for Selena Guardrails
"""

class QuantEngine:
    def __init__(self, target_slippage_bps=50):
        self.target_slippage_bps = target_slippage_bps

    def calculate_trade_metrics(self, trade_amount_sol: float, pool_price_usd: float, pool_liquidity_usd: float) -> dict:
        trade_value_usd = trade_amount_sol * pool_price_usd
        
        if pool_liquidity_usd <= 0:
            return {"error": "Insufficient Liquidity", "is_safe": False}
            
        # Constant Product Price Impact Calculation
        price_impact_raw = trade_value_usd / (pool_liquidity_usd + trade_value_usd)
        price_impact_percentage = round(price_impact_raw * 100, 4)

        expected_output_usd = trade_value_usd * (1 - price_impact_raw)
        slippage_tolerance_decimal = self.target_slippage_bps / 10000
        min_received_usd = expected_output_usd * (1 - slippage_tolerance_decimal)

        return {
            "status": "SUCCESS",
            "trade_value_usd": round(trade_value_usd, 2),
            "price_impact_percent": price_impact_percentage,
            "min_received_usd": round(min_received_usd, 2),
            "is_safe": price_impact_percentage <= (self.target_slippage_bps / 100)
        }