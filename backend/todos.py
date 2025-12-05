from fastapi import APIRouter, Depends, Request, HTTPException

from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Todo
from schemas import (
    TodoCreate,
    TodoUpdate,
    TodoResponse,
    TodoCreateResponse,
    TodoUpdateResponse,
    TodoDeleteResponse,
)
from auth import require_api_key
from logger import logger


router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/read", response_model=List[TodoResponse])
@require_api_key
async def read_todos(
    request: Request,
    db: Session = Depends(get_db),
):
    logger.info("Fetching all todos")
    todos = db.query(Todo).all()
    logger.info(f"Found {len(todos)} todos")
    return todos


# TODO: Create a endpoint to filter & read a specific todo


@router.post("/create", response_model=TodoCreateResponse)
@require_api_key
async def create_todo(
    request: Request,
    todo: TodoCreate,
    db: Session = Depends(get_db),
):
    logger.info(f"Creating todo: {todo.name}")
    try:
        db_todo = Todo(
            name=todo.name,
            order=todo.order,
            completed=todo.completed,
        )
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)

        todos = db.query(Todo).all()

        logger.info(f"Todo created successfully with id: {db_todo.id}")
        return {
            "success": True,
            "created_todo": db_todo,
            "todos": todos,
            "error": None,
        }
    except Exception as e:
        db.rollback()
        todos = db.query(Todo).all()

        logger.error(f"Failed to create todo: {str(e)}")
        return {
            "success": False,
            "created_todo": None,
            "todos": todos,
            "error": str(e),
        }


@router.patch("/update/{todo_id}", response_model=TodoUpdateResponse)
@require_api_key
async def update_todo(
    request: Request,
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db),
):
    logger.info(f"Updating todo with id: {todo_id}")
    try:
        db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if not db_todo:
            logger.warning(f"Todo with id {todo_id} not found")
            raise HTTPException(status_code=404, detail="Todo not found")

        update_data = todo.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_todo, key, value)

        db.commit()
        db.refresh(db_todo)

        todos = db.query(Todo).all()

        logger.info(f"Todo {todo_id} updated successfully")
        return {
            "success": True,
            "updated_todo": db_todo,
            "todos": todos,
            "error": None,
        }

    except Exception as e:
        db.rollback()
        todos = db.query(Todo).all()

        logger.error(f"Failed to update todo {todo_id}: {str(e)}")
        return {
            "success": False,
            "updated_todo": None,
            "todos": todos,
            "error": str(e),
        }


@router.delete("/delete/{todo_id}", response_model=TodoDeleteResponse)
@require_api_key
async def delete_todo(
    request: Request,
    todo_id: int,
    db: Session = Depends(get_db),
):
    logger.info(f"Deleting todo with id: {todo_id}")
    try:
        db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if not db_todo:
            logger.warning(f"Todo with id {todo_id} not found")
            raise HTTPException(status_code=404, detail="Todo not found")

        deleted_todo = TodoResponse(
            id=db_todo.id,
            name=db_todo.name,
            order=db_todo.order,
            completed=db_todo.completed,
        )

        db.delete(db_todo)
        db.commit()

        todos = db.query(Todo).all()

        logger.info(f"Todo {todo_id} deleted successfully")
        return {
            "success": True,
            "deleted_todo": deleted_todo,
            "todos": todos,
            "error": None,
        }

    except Exception as e:
        db.rollback()
        todos = db.query(Todo).all()

        logger.error(f"Failed to delete todo {todo_id}: {str(e)}")
        return {
            "success": False,
            "deleted_todo": None,
            "todos": todos,
            "error": str(e),
        }
