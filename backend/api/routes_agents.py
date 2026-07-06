
from fastapi import APIRouter
from backend.orchestrator.agent_orchestrator import AgentOrchestrator

router = APIRouter()
orchestrator = AgentOrchestrator()

@router.post("/run")
def run_agents(payload: dict):
    text = payload.get("text")

    result = orchestrator.run_pipeline(text)

    return result
