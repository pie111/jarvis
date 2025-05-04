from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from api.v1.endpoints import router as agent_router
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from contextlib import asynccontextmanager
from db.models import Base
from db.session import DatabaseManager
from sqlalchemy.exc import OperationalError


@asynccontextmanager
async def lifespan(app: FastAPI):
    """ This event is triggered when the app starts """
    try:
        logger.info("Checking database connection...")
        session_factory = DatabaseManager.get_session_factory()
        # Try to create a session and connect to the DB
        with session_factory() as session:
            # You can also use `session.execute("SELECT 1")` or `session.query` to ensure the DB is up
            result = session.execute(text("SELECT 1"))
            result.fetchone()
        
        logger.info("Database is up.")
        yield
    except OperationalError as e:
        logger.error("Database connection failed!")
        logger.error(e)
        raise RuntimeError("Cannot start app: Database is unreachable") from e


app = FastAPI(
    title="Jarvis",
    description="An AI agentic companion",
    version="0.1.0",
    lifespan=lifespan
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