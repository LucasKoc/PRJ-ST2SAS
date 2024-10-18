from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, String, Integer, Boolean, JSON

from backend.api.core.settings import Settings
from backend.api.database.database import Base

class StudentModel(BaseModel):
    student_id: int
    first_name: str
    last_name: str
    school_email: str
    phone: Optional[str] = None
    picture_path: Optional[str] = None


class StudentModelDB(Base):
    __tablename__ = "students"
    __table_args__ = {"schema": Settings.POSTGRES_SCHEMA}

    student_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    school_email = Column(String)
    phone = Column(String, default=None)
    picture_path = Column(String, default=None)
