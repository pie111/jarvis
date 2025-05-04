from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, Engine, event
from core.config import settings
from typing import Type
from loguru import logger


    
class DatabaseManager:
    """
    Database manager class for managing database sessions.
    """
    _session_factory: Type[sessionmaker] = None

    @staticmethod
    def get_engine_config():
        """
        Gets the SQLAlchemy engine config from environment variables.
        """
        if settings.DATABASE_URL:
            return {"url" : settings.DATABASE_URL, 'pool_size': int(settings.DB_POOL_SIZE) , 'max_overflow': int(settings.MAX_OVERFLOW)}
        else:
            raise ValueError("DATABASE_URL is not set in environment variables")
        
    @staticmethod
    def get_engine():
        """
        Create a SQLAlchemy engine from environment variables.
        """
        db_config = DatabaseManager.get_engine_config()
        engine: Engine = create_engine(**db_config)
        return engine
    
    @classmethod
    def get_session_factory(cls) -> Type[sessionmaker]:
        """
        Get or create a session factory.
        Returns a factory function that creates new database sessions.
        """
        if cls._session_factory is None:
            logger.info("Creating session factory...")
            # Create the session factory once and reuse it
            cls._session_factory = sessionmaker(bind=cls().get_engine())
            logger.info("Session factory created successfully")
        return cls._session_factory








# A sample function to refer the db usage and TODO: it needs to be removed once the usage is done
def example_function():
    # Get the session factory (a function that creates new sessions)
    logger.info("Getting session factory...")
    session_factory = DatabaseManager.get_session_factory()
    
    # Create a new session - this is when the actual connection is established
    logger.info("Creating new session...")
    session: Session = session_factory()
    
    try:
        # Use the session
        result = session.execute("SELECT 1")
        print(result.scalar())
    finally:
        # Always close the session when done
        logger.info("Closing session...")
        session.close()


