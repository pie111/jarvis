from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional




class ToolConfig(BaseModel):
    name: str
    description: str
    command: str
    args: list[str]
    env: Optional[dict]
    transport: str = "stdio"
    # Add other fields for the tool configuration if needed


class ToolResponse(BaseModel):
    id: int
    name: str
    account_id: Optional[str]
    config: dict
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True) 