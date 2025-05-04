from fastapi import HTTPException
from db.models import Tools
from exceptions.tool import ToolNotFoundError


class ToolsDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self,limit : int=0,offset:int =0):
        """Get all tools."""
        query = self.session.query(Tools)
        if limit > 0:
            query = query.limit(limit)
        if offset > 0:
            query = query.offset(offset)
        return query.all()
    
    def get_by_id(self,id):
        """Get a tool by its ID."""
        return self.session.query(Tools).filter(Tools.id==id)
    
    def create(self, tool_data):
        """Create a new tool."""
        tool = Tools(**tool_data)
        self.session.add(tool)
        return tool
    
    def update(self, tool_id, updated_tool_data):
        """Update an existing tool."""""
        tool = self.get_by_id(tool_id)
        for key, value in updated_tool_data.items():
            setattr(tool, key, value)
        return tool


    def upsert(self, tool_data):
        """Update an existing tool if it exists, otherwise create a new one."""""
        existing_tool = self.get_by_id(tool_data["id"])
        if existing_tool:
            for key, value in tool_data.items():
                setattr(existing_tool, key, value)
        else:
            new_tool = Tools(**tool_data)
            self.session.add(new_tool)
        return existing_tool or new_tool


    def delete(self, tool_id):
        """Delete a tool by its ID."""""
        tool = self.get_by_id(tool_id)
        if not tool:
            raise ToolNotFoundError(tool_id)
        self.session.delete(tool)
        return tool_id