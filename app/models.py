from database import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from datetime import datetime


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    is_completed = Column(Boolean, nullable=False)
    time_created = Column(DateTime, default=datetime.utcnow)
