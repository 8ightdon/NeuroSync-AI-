from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ToolCall(BaseModel):
    tool_name: str
    parameters: dict

@router.get("/")
def list_tools():
    # Return available tools
    return {"tools": ["web_search", "code_exec"]}

@router.post("/call")
def call_tool(call: ToolCall):
    # Call the specified tool
    return {"result": f"Called {call.tool_name} with {call.parameters}"} 