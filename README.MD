# Jarvis - AI Agent System

A production-ready AI agent system built with FastAPI that enables dynamic tool integration and intelligent task execution. The system uses LangChain and the Model Context Protocol (MCP) to create flexible AI agents that can interact with various tools and services.

## Features

- **Dynamic Tool Integration**: Supports multiple tools including:
  - Mathematical computations
  - PostgreSQL database operations 
  - Tavily search integration
  - Timezone handling
- **Reactive Agent Architecture**: Built on LangChain's React pattern for intelligent decision making
- **Database Management**: SQLAlchemy ORM with proper tool management and persistence
- **Production Ready**: Built with FastAPI for high performance and scalability

## Tech Stack

- FastAPI
- SQLAlchemy
- LangChain
- Model Context Protocol (MCP)
- PostgreSQL
- Python 3.12+

## Local Development Setup

1. **Prerequisites**
   - Python 3.12+
   - Poetry for dependency management
   - PostgreSQL database
   - Node.js and npm (for certain MCP tools)

2. **Environment Setup**
   ```bash
   # Clone the repository
   git clone <repository-url>
   cd jarvis

   # Install dependencies using Poetry
   poetry install
   ```

3. **Database Setup**
   ```bash
   # Create a PostgreSQL database
   createdb jarvis

   ```

4. **Environment Variables**
   Create a `.env` file with:
   ```
   TAVILY_API_KEY=your_tavily_api_key
   DATABASE_URL=your_db_connection
   ```

5. **Running the Application**
   ```bash
   # Start the FastAPI server
   poetry run uvicorn main:app --reload
   ```

## Project Structure
- `main.py`: The main entry point of your application.
- `services/mcp_servers/math_server.py`: A simple math server for testing purposes.
- `services/mcp.py`: Your MCP implementation, which includes the necessary components to interact with other services.
