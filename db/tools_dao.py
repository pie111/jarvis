from db.models import Tools


class ToolsDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Get all tools."""
        return self.session.query(Tools).all()
    
    def get_by_id(self,id):
        """Get a tool by its ID."""
        return self.session.query(Tools).filter(Tools.id==id)
    
    def create(self, tool_data):
        """Create a new tool."""
        tool = Tools(**tool_data)
        self.session.add(tool)
        self.session.commit()
        return tool
    
    def update(self, tool_id, updated_tool_data):
        """Update an existing tool."""""
        tool = self.get_by_id(tool_id)
        for key, value in updated_tool_data.items():
            setattr(tool, key, value)
        self.session.commit()


    def upsert(self, tool_data):
        """Update an existing tool if it exists, otherwise create a new one."""""
        existing_tool = self.get_by_id(tool_data["id"])
        if existing_tool:
            for key, value in tool_data.items():
                setattr(existing_tool, key, value)
        else:
            new_tool = Tools(**tool_data)
            self.session.add(new_tool)
            self.session.commit()
        return existing_tool or new_tool


    def delete(self, tool_id):
        """Delete a tool by its ID."""""
        tool = self.get_by_id(tool_id)
        self.session.delete(tool)
        self.session.commit()
        return tool_id