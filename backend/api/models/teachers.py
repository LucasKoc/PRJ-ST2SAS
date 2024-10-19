from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Boolean, JSON

from backend.api.core.settings import Settings
from backend.api.database.database import Base

class TeacherModel(BaseModel):
    teacher_id: str
    first_name: str
    last_name: str
    school_email: str
    phone: Optional[str] = None
    speciality: str
    picture_path: Optional[str] = None

class TeacherModelDB(Base):
    __tablename__ = "teachers"
    __table_args__ = {"schema": Settings.POSTGRES_SCHEMA}

    teacher_id = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    school_email = Column(String)
    phone = Column(String, default=None)
    speciality = Column(String)
    picture_path = Column(String, default=None)
