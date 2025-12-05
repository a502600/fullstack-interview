# Todo API Backend

A RESTful API for managing todos built with FastAPI, SQLAlchemy, and SQLite.

## Tech Stack

- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Alembic** - Database migrations
- **SQLite** - Lightweight database
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server

## Project Structure

```
backend/
├── main.py          # FastAPI app initialization and middleware
├── config.py        # Environment configuration
├── database.py      # Database connection and session
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas for request/response
├── todos.py         # Todo endpoints router
├── auth.py          # API key authentication
├── alembic/         # Database migrations
│   ├── env.py       # Alembic environment config
│   └── versions/    # Migration scripts
├── alembic.ini      # Alembic configuration
├── requirements.txt # Python dependencies
├── request.http     # Example HTTP requests
└── session.sql      # SQL queries reference
```

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```env
DB_NAME=sqlite.db
FRONTEND_URL=http://localhost:3000
X_API_KEY=your-api-key
```

4. Run database migrations:
```bash
alembic upgrade head
```

5. Run the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## Database Migrations

This project uses Alembic for database migrations.

### Apply migrations
```bash
alembic upgrade head
```

### Create a new migration (after model changes)
```bash
alembic revision --autogenerate -m "description of changes"
```

### View migration history
```bash
alembic history
```

### Downgrade (rollback) last migration
```bash
alembic downgrade -1
```

### Downgrade to specific revision
```bash
alembic downgrade <revision_id>
```

## API Endpoints

All endpoints require the `X-API-Key` header for authentication.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/todos/read` | Get all todos |
| POST | `/todos/create` | Create a new todo |
| PATCH | `/todos/update/{id}` | Update a todo |
| DELETE | `/todos/delete/{id}` | Delete a todo |

## Request Examples

### Get all todos
```http
GET /todos/read
X-API-Key: your-api-key
```

### Create a todo
```http
POST /todos/create
X-API-Key: your-api-key
Content-Type: application/json

{
    "name": "Buy groceries",
    "order": 1,
    "completed": false
}
```

### Update a todo
```http
PATCH /todos/update/1
X-API-Key: your-api-key
Content-Type: application/json

{
    "completed": true
}
```

### Delete a todo
```http
DELETE /todos/delete/1
X-API-Key: your-api-key
```

## Response Format

### Success Response (Create/Update/Delete)
```json
{
    "success": true,
    "created_todo": { "id": 1, "name": "...", "order": 1, "completed": false },
    "todos": [...],
    "error": null
}
```

### Error Response
```json
{
    "success": false,
    "created_todo": null,
    "todos": [...],
    "error": "Error message"
}
```

## API Documentation

FastAPI provides automatic interactive documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
