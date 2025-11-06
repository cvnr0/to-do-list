from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    is_done: bool
    created_at: datetime

class Config:
    orm_mode = True

