from fastapi import FastAPI
from routes import task

app = FastAPI(title="Task Manager API",
    description="This is an API created to manage tasks with FastAPI.",
    version="1.0.0"
)

app.include_router(task.router)
