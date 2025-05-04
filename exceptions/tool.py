class ToolNotFoundError(Exception):
    """Raised when a tool with the given ID is not found."""
    def __init__(self, tool_id: int):
        self.tool_id = tool_id
        self.message = f"Tool with ID {tool_id} not found"
        super().__init__(self.message)