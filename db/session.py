from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, Engine, event
from core.config import settings
from db.session import database_manager
from typing import Type
from loguru import logger

class DatabaseManager:
    """
    Database manager class for managing database sessions.
    """
    _session_factory: Type[sessionmaker] = None


    def get_engine_config(self):
        """
        Create a SQLAlchemy engine from environment variables.
        """
        if settings.DATABASE_URL:
            return {"url" : settings.DATABASE_URL, 'pool_size': int(settings.DB_POOL_SIZE) , 'max_overflow': int(settings.MAX_OVERFLOW)}
        else:
            raise ValueError("DATABASE_URL is not set in environment variables")
        

    def get_engine(self):
        """
        Create a SQLAlchemy engine from environment variables.
        """
        db_config = self.get_engine_config()
        engine: Engine = create_engine(**db_config)
        @event.listens_for(engine, "connect")
        def do_connect(connection,record):
            logger.info("New database connection established!")
            try:
                connection.execute("SELECT 1")
            except Exception as e:
                logger.error(f"Error executing query on {engine}: {e}")
        return engine
    

    def get_session_factory(self) -> Type[sessionmaker]:
        """
        Get or create a session factory.
        Returns a factory function that creates new database sessions.
        """
        if self._session_factory is None:
            logger.info("Creating session factory...")
            # Create the session factory once and reuse it
            self._session_factory = sessionmaker(bind=self.get_engine())
            logger.info("Session factory created successfully")
        return self._session_factory







# A sample function to refer the db usage and TODO: it needs to be removed once the usage is done
def example_function():
    # Get the session factory (a function that creates new sessions)
    logger.info("Getting session factory...")
    session_factory = DatabaseManager().get_session_factory()
    
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


