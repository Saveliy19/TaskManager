from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.models import NewTask, Task, Tasks

router = APIRouter()

tasks = []
next_id = 1

@router.post("/task")
async def create_task(new_task: NewTask):
    global next_id
    task = Task(id = next_id, **new_task.model_dump())
    tasks.append(task)
    print(tasks)
    next_id += 1
    return JSONResponse(content={"id": task.id}, status_code=201)

@router.get("/tasks", response_model = Tasks)
async def get_tasks():
    return Tasks(tasks=tasks)

@router.put("/task")
async def update_task(task: Task):
    try:
        tasks[task.id - 1] = task
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    try:
        del tasks[task_id - 1]
        return 
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)