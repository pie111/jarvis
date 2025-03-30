from typing import List
from mcp.server.fastmcp import FastMCP

# Create the FastMCP instance
mcp = FastMCP("Weather")

# Configure the port
mcp.config.port = 8001

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return "It's always sunny in New York"

if __name__ == "__main__":
    mcp.run(transport="sse")