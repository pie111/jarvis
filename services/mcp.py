import dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.checkpoint.memory import MemorySaver
import asyncio
from langchain.agents import AgentExecutor
from services.llm_service import get_llm
from langgraph.prebuilt import create_react_agent
from core.prompts import syst_prompt
from langchain import hub
import uuid
from loguru import logger
from core.config import settings
import os
memory = MemorySaver()
from dotenv import load_dotenv
load_dotenv()

class ReactiveAgent:
    def __init__(self, llm_model: str): 
        self.llm = get_llm(llm_model)
        self.tools = []
        self.syst_prompt = hub.pull("hwchase17/react")
       
    
    async def _run_async(self,message,thread_id:str):
        async with MultiServerMCPClient(
            {
                "math": {
                    "command": "python",
                    # Make sure to update to the full absolute path to your math_server.py file
                    "args": ["services/mcp_servers/math_server.py"],
                    "transport": "stdio",
                },
                "postgres": {
                    "command": "npx",
                    # Make sure to update to the full absolute path to your math_server.py file
                    "args": ["-y", "@modelcontextprotocol/server-postgres", settings.MCP_POSTGRES_CONN_URL ],
                    "transport": "stdio",
                },
                "tavily": {
                    "command": "npx",
                    "args": ["-y", "@mcptools/mcp-tavily"],
                    "env": dict(os.environ, TAVILY_API_KEY=str(settings.TAVILY_API_KEY)),
                    "transport": "stdio"
                },
                "timezone": {
                    "command": "python",
                    "args": ["-m", "mcp_server_time", "--local-timezone=Asia/Kolkata"],
                    "transport": "stdio"
                }
            }
        ) as client:
            tools = client.get_tools()
            
            thread_id = thread_id or str(uuid.uuid4())
            config = {"configurable": {"thread_id":thread_id }}
            agent = create_react_agent(self.llm,tools,checkpointer=memory)
            inputs = {"messages": [("user", message)]}
            response = await agent.ainvoke(inputs, config=config)
            logger.info(response)
            last_message = response.get("messages")[-1]
            return last_message