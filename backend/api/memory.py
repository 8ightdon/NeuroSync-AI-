from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class MemoryItem(BaseModel):
    user_id: str
    content: str
    embedding: list = []

@router.get("/")
def get_memory(user_id: str):
    # Fetch memory from DB/vector store
    return {"memory": []}

@router.post("/")
def add_memory(item: MemoryItem):
    # Add memory to DB/vector store
    return {"status": "added"} 