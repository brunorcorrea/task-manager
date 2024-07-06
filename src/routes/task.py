from fastapi import APIRouter, HTTPException
from models.task import Task

router = APIRouter(tags=["Task"])

tasks = []

BASE_URL = "/tasks"
CREATE_TASK_URL = BASE_URL
LIST_TASKS_URL = BASE_URL
FIND_TASK_BY_ID_URL = BASE_URL + "/{task_id}"
UPDATE_TASK_BY_ID_URL = BASE_URL + "/{task_id}"
DELETE_TASK_BY_ID_URL = BASE_URL + "/{task_id}"

@router.post(CREATE_TASK_URL, response_model=Task)
async def create_tasks(task: Task):
    tasks.append(task)
    return task

@router.get(LIST_TASKS_URL, response_model=list[Task])
async def get_tasks():
    return tasks

@router.get(FIND_TASK_BY_ID_URL, response_model=Task)
async def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put(UPDATE_TASK_BY_ID_URL, response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete(DELETE_TASK_BY_ID_URL, response_model=Task)
async def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(index)
    raise HTTPException(status_code=404, detail="Task not found")
