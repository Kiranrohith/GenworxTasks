from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel,Field

app = FastAPI()

tasks = []
next_id = 1

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(max_length= 500)

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)
    completed: bool | None = None

@app.post("/tasks", response_model=TaskResponse, status_code= status.HTTP_201_CREATED)
def create_task(task:TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "completed": False
    }

    tasks.append(new_task)
    next_id+=1

    return new_task

@app.get("/tasks",response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}",response_model=TaskResponse, status_code=status.HTTP_200_OK)
def get_task(task_id:int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )

@app.put("/tasks/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id:int, updated_task:TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:

            if updated_task.title is not None:
                task["title"] = updated_task.title
            if updated_task.description is not None:
                task["description"] = updated_task.description
            if updated_task.completed is not None:
                task["completed"] = updated_task.completed

            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )

@app.delete("/tasks/{task_id}",status_code=status.HTTP_200_OK)
def delete_task(task_id:int):
    for index, task in enumerate(tasks):

        if task["id"] == task_id:
            return tasks.pop(index)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )

