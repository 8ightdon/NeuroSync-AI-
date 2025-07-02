# NeuroSync AI Backend

This is the FastAPI backend for NeuroSync AI. It handles API endpoints, model inference, memory, tool plugins, and integrations.

## Structure
- `main.py` — FastAPI app entrypoint
- `api/` — API routes (chat, memory, tools, users, logs)
- `models/` — Model inference and prompt engineering
- `memory/` — Short-term and persistent memory logic
- `tools/` — Tool/plugin definitions
- `integrations/` — WhatsApp/Telegram, etc.
- `core/` — Utilities, context, security, etc.

## Quickstart
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `uvicorn main:app --reload --host 0.0.0.0 --port 8000` 