from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from services.llm_service import get_llm
from services.vector_service import VectorService
from services.embedding_service import get_embedding_model
from langgraph.graph.message import add_messages
from langchain.schema import AIMessage
from langchain_core.messages import HumanMessage, SystemMessage
from core.prompts import syst_prompt
from langgraph.prebuilt import ToolNode


# Define the state structure for the graph
class GraphState(TypedDict):
    messages: Annotated[list, add_messages]
    isMcpTool: bool = False  # Set default value to False





class GraphService:
    def __init__(self, llm_model: str, embedding_model: str):
        self.llm = get_llm(llm_model)
        self.vector_service = VectorService(embedding_model)
        self.workflow = self._build_workflow()
        self.tools = []
        self.tool_node = ToolNode(self.tools)

    def _process_query(self, state: GraphState) -> GraphState:
        """Node to process the initial query."""
        return {"query": state["query"], "context": "", "response": ""}

    def _retrieve_context(self, state: GraphState) -> GraphState:
        """Node to retrieve context from the vector store."""
        context_docs = self.vector_service.search(state["query"], k=2)
        context = "\n".join(context_docs)
        return {"query": state["query"], "context": context, "response": ""}

    def _generate_response(self, state: GraphState) -> GraphState:
        """Node to generate a response using the LLM."""
        prompt = f"Context:\n{state['context']}\n\nQuestion: {state['query']}"
        response = self.llm.invoke(prompt)
        return {"query": state["query"], "context": state["context"], "response": response}
    
    def chatnode(self, state :StateGraph) -> GraphState:
        "Node responsible for the chatting interaction"
        messages = state["messages"]
        last_message = messages[-1]
        # If last message is a tool result, generate a response
        if isinstance(last_message, HumanMessage):
            # Initial invocation for tool calls
            response = self.llm.invoke(syst_prompt.format_messages(user_input=messages))
            state["messages"].append(response)
        
        return state
    
    def tool_node(self,state: StateGraph) -> GraphState:
        messages = state["messages"]
        last_message = messages[-1]
        if hasattr(last_message,'tool_calls') and last_message.tool_calls:
            tool_res = ToolNode(last_message['tools'])
            state["messages"].append(AIMessage(content=tool_res))
            return state


    def _build_workflow(self) -> StateGraph:
        """Build the LangGraph workflow with nodes and edges."""
        graph = StateGraph(GraphState)

        # Add nodes
        graph.add_node("process_query", self._process_query)
        graph.add_node("retrieve_context", self._retrieve_context)
        graph.add_node("generate_response", self._generate_response)

        # Define edges (sequential flow)
        graph.add_edge("process_query", "retrieve_context")
        graph.add_edge("retrieve_context", "generate_response")
        graph.add_edge("generate_response", END)

        # Set the entry point
        graph.set_entry_point("process_query")

        # Compile the graph
        return graph.compile()

    def run(self, query: str) -> dict:
        """Run the workflow for a given query."""
        initial_state = {"query": query, "context": "", "response": ""}
        result = self.workflow.invoke(initial_state)
        return result


    graph_service = GraphService(
        llm_model="openai/gpt-4",
        embedding_model="openai/text-embedding-ada-002"
    )
    
    # Add some sample data to the vector store
    from services.vector_service import vector_service
    vector_service.add_documents(["AI is amazing.", "Graphs are powerful tools."])
    
    # Run the workflow
    result = graph_service.run("What is AI?")
    print(result)