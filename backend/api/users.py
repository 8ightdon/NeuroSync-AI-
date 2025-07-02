from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    username: str
    id: str = None

@router.post("/")
def create_user(user: User):
    # Add user to DB
    return {"status": "created", "user": user}

@router.get("/")
def list_users():
    # List users from DB
    return {"users": []} 