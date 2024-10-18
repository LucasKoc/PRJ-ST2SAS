from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.database.database import get_db
from backend.api.models.teachers import TeacherModel, TeacherModelDB

router = APIRouter()

@router.post("/", response_model=TeacherModel)
def create_teacher_request(student: TeacherModel, db: Session = Depends(get_db)):
    return HTTPException(status_code=501, detail="Not implemented")

@router.get("/", response_model=List[TeacherModel])
def read_teachers_request(db: Session = Depends(get_db)):
    return HTTPException(status_code=501, detail="Not implemented")

@router.get("/{teacher_id}", response_model=TeacherModel)
def read_teacher_request(teacher_id: str, db: Session = Depends(get_db)):
    return HTTPException(status_code=501, detail="Not implemented")
