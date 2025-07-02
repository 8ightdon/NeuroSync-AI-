from fastapi import APIRouter, WebSocket, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import AsyncGenerator

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str
    session_id: str = None

@router.post("/")
async def chat_endpoint(request: ChatRequest):
    # Inject context, memory, and call model inference here
    response = f"[AI] You said: {request.message}"
    return {"response": response}

@router.websocket("/stream")
async def chat_stream(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Stream response token by token (placeholder)
        for token in ["[AI]", " ", "You", " ", "said:", " ", data]:
            await websocket.send_text(token) 