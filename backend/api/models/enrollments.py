from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Boolean, JSON

from backend.api.core.settings import Settings
from backend.api.database.database import Base

class EnrollmentModel(BaseModel):
    student_id: int
    course_id: str
    grade: Optional[int] = None

class EnrollmentModelDB(Base):
    __tablename__ = "enrollments"
    __table_args__ = {"schema": Settings.POSTGRES_SCHEMA}

    student_id = Column(Integer, primary_key=True, index=True)
    course_id = Column(String, primary_key=True, index=True)
    grade = Column(Integer, default=None)
