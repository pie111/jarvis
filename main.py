from fastapi import FastAPI
from api.v1.endpoints import router as agent_router

app = FastAPI(
    title="Jarvis",
    description="An AI agentic companion",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "Welcome to Jarvis"}

app.include_router(agent_router, prefix="/api/v1")