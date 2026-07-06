from backend.services.llm_service import analyze_contract
from backend.agents.base_agent import BaseAgent

class ContractAgent(BaseAgent):

    def run(self, text):
        return analyze_contract(text)
