from pydantic import BaseModel
from datetime import datetime

from typing import List

class NewTask(BaseModel):
    header: str
    description: str
    deadline: datetime

class Task(NewTask):
    id: int

class Tasks(BaseModel):
    tasks: List[Task]