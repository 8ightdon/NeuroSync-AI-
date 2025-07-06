
.PHONY: up down build logs frontend backend test-backend test-frontend

up:
	docker-compose up --build

down:
	docker-compose down

build:
	docker-compose build

logs:
	docker-compose logs -f

frontend:
	cd frontend && npm run dev

backend:
	cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

test-backend:
	cd backend && pytest

test-frontend:
	cd frontend && npm run test

