from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import TaskCreate, TaskResponse, TaskUpdate
from services import create_task_res, delete_task_res, get_task_res, get_tasks_res, update_task_res

serviceRouter = APIRouter()


@serviceRouter.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    try:
        return create_task_res(db, task)
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Database error occurred")


@serviceRouter.get("/tasks", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
def get_tasks(db: Session = Depends(get_db)):
    try:
        return get_tasks_res(db)
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Database error occurred")


@serviceRouter.get("/tasks/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def get_task(task_id: int, db: Session = Depends(get_db)):
    try:
        return get_task_res(db, task_id)
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Database error occurred")


@serviceRouter.put("/tasks/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id: int, updated_task: TaskUpdate, db: Session = Depends(get_db)):
    try:
        return update_task_res(db, task_id, updated_task)
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Database error occurred")


@serviceRouter.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        return delete_task_res(db, task_id)
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Database error occurred")
