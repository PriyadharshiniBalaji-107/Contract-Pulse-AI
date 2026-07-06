class RevenueAgent:

    def run(self, contract_data):
        if "billing" not in str(contract_data).lower():
            return {
                "revenue_risk": "Possible leakage detected"
            }

        return {
            "revenue_risk": "No issue detected"
        }
