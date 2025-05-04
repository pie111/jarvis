from models.tool import ToolConfig

def get_tool_data_to_save(toolconfig : ToolConfig):
    tool_dict = toolconfig.model_dump()
    tool_info = {
        "name": tool_dict["name"],
        "config": {
            "command": tool_dict["command"],
            "args": tool_dict["args"],
            "env": tool_dict.get("env", None),
            "transport": tool_dict.get("transport", "stdio"),
        }
    }
    return tool_info
