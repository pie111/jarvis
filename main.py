from fastapi import FastAPI
from api.v1.endpoints import router as agent_router
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from contextlib import asynccontextmanager
from db.models import Base



app = FastAPI(
    title="Jarvis",
    description="An AI agentic companion",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Jarvis"}

app.include_router(agent_router, prefix="/api/v1")