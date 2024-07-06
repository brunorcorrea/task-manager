from pydantic import BaseModel
from datetime import date

class Task(BaseModel):
    id: int
    title: str
    description: str
    due_date: date
    completed: bool = False
    completed_date: date = None
