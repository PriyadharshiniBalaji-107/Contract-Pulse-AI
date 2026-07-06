from fastapi import FastAPI
from backend.api.routes_contract import router as contract_router
from backend.api.routes_agents import router as agent_router

app = FastAPI(title="Contract Pulse AI")

app.include_router(contract_router, prefix="/contract")
app.include_router(agent_router, prefix="/agents")

@app.get("/")
def home():
    return {"message": "Contract Pulse AI is running"}
