from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.database.database import get_db
from backend.api.models.courses import CourseModel, CourseModelDB

router = APIRouter()

@router.post("/", response_model=CourseModel)
def create_course_request(student: CourseModel, db: Session = Depends(get_db)):
    return HTTPException(status_code=501, detail="Not implemented")

@router.get("/", response_model=List[CourseModel])
def read_courses_request(db: Session = Depends(get_db)):
    return HTTPException(status_code=501, detail="Not implemented")

@router.get("/{course_id}", response_model=CourseModel)
def read_course_request(course_id: str, db: Session = Depends(get_db)):
    return HTTPException(status_code=501, detail="Not implemented")
