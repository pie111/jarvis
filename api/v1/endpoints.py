from fastapi import HTTPException,APIRouter
from loguru import logger
from core.config import settings
from services.mcp import ReactiveAgent
from utils import messages
from models.tool import ToolConfig, ToolResponse
from db.session import DatabaseManager
from db.tools_dao import ToolsDAO
from utils.tool_utils import get_tool_data_to_save

router = APIRouter()


@router.post('/chat')
async def chat(
    query: str,
    thread_id: str
):
    try: 
        model =settings.DEFAULT_LLM_MODEL
        logger.info("Entering the chat function")
        reactive_agent = ReactiveAgent(model)
        user_message = await reactive_agent._run_async(query,thread_id)
        return user_message
    except Exception as e:
        logger.info(f"Error during cleanup: {str(e)}")
        return HTTPException(status_code=500, detail=messages.HTTP_500_INTERNAL_SERVER_ERROR)
    



@router.post('/tool',response_model=ToolResponse)
async def create_tool(
    tool_data: ToolConfig,
):
    session_factory = DatabaseManager.get_session_factory()
    with session_factory() as session:
        try:
            logger.info("Creating new tool...")
            tool_dao = ToolsDAO(session)  # Renamed 'tool_ao' to 'tool_dao'
            tool_dict = get_tool_data_to_save(tool_data)
            tool = tool_dao.create(tool_dict)  # Renamed 'toolDao' to 'tool_dao'
            logger.info(f"Tool created with ID: {tool.id}")
            session.commit()
            return ToolResponse.model_validate(tool)
        except Exception as e:
            logger.info(f"Error during cleanup: {str(e)}")
            session.rollback()
            raise HTTPException(status_code=500, detail=messages.HTTP_500_INTERNAL_SERVER_ERROR)
        
    

@router.get('/tools')
async def get_tools(limit:int=0,offset:int=0):
    session_factory = DatabaseManager.get_session_factory()
    with session_factory() as session:
        try:
            logger.info("Getting all tools...")            
            tool_dao = ToolsDAO(session)
            tools = tool_dao.get_all(limit,offset)
            return tools
        except Exception as e:
            logger.info(f"Error during cleanup: {str(e)}")
            raise HTTPException(status_code=500, detail=messages.HTTP_500_INTERNAL_SERVER_ERROR)