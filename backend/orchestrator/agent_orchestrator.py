from backend.agents.contract_agent import ContractAgent
from backend.agents.risk_agent import RiskAgent
from backend.agents.revenue_agent import RevenueAgent

class AgentOrchestrator:

    def __init__(self):
        self.contract_agent = ContractAgent()
        self.risk_agent = RiskAgent()
        self.revenue_agent = RevenueAgent()

    def run_pipeline(self, text):

        contract_data = self.contract_agent.run(text)
        risk_data = self.risk_agent.run(contract_data)
        revenue_data = self.revenue_agent.run(contract_data)

        return {
            "contract": contract_data,
            "risk": risk_data,
            "revenue": revenue_data
        }
