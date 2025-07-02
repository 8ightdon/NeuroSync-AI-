from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from backend.api import chat, memory, tools, users, logs

app = FastAPI(title="NeuroSync AI Backend")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include modular routers
app.include_router(chat.router, prefix="/chat")
app.include_router(memory.router, prefix="/memory")
app.include_router(tools.router, prefix="/tools")
app.include_router(users.router, prefix="/users")
app.include_router(logs.router, prefix="/logs")

@app.get("/")
def root():
    return {"message": "NeuroSync AI Backend is running!"}

# Example WebSocket for streaming
@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Here, you would stream model output token by token
        await websocket.send_text(f"Echo: {data}") 