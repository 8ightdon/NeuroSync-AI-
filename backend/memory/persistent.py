# Persistent memory (Postgres/Chroma vector DB)

from sqlalchemy.orm import Session

class PersistentMemory:
    def __init__(self, db: Session):
        self.db = db

    def add(self, user_id, content, embedding):
        # Store content and embedding in DB
        pass

    def search(self, user_id, query_embedding):
        # Search for similar embeddings/content
        return [] 