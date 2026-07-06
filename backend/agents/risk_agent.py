class RiskAgent:

    def run(self, contract_data):
        risk_score = 0

        if "penalty" in str(contract_data).lower():
            risk_score += 30

        if "renewal" not in str(contract_data).lower():
            risk_score += 20

        return {
            "risk_score": min(risk_score, 100),
            "risk_level": "HIGH" if risk_score > 50 else "LOW"
        }
