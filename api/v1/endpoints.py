from fastapi import HTTPException,APIRouter
from loguru import logger
from core.config import settings
from services.mcp import ReactiveAgent
from utils import messages

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
    

@router.post('/tool')
async def create_tool(
    tool_data: dict,
):
    #TODO: Implement the logic to create a new tool
    pass