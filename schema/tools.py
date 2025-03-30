from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from enum import Enum

class TransportType(str, Enum):
    """Transport types supported for tool communication."""
    sse = 'sse'    # Server-Sent Events
    stdio = 'stdio'  # Standard Input/Output


class CreateTool(BaseModel):
    """A specification for a tool that can be used in an agent.
    
    Attributes:
        name: Unique identifier for the tool
        command: The command to execute (e.g., 'python', 'npx')
        args: List of arguments to pass to the command
        transport: Communication method (sse or stdio)
        env: Optional environment variables for the tool
        description: Optional description of what the tool does
    """
    name: str
    command: str
    args: List[str]
    transport: TransportType
    env: Optional[Dict[str, str]] = None
    description: Optional[str] = Field(None, max_length=500)