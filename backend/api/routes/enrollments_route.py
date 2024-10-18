from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.database.database import get_db
from backend.api.models.enrollments import EnrollmentModel, EnrollmentModelDB

router = APIRouter()

@router.post("/", response_model=EnrollmentModel)
def create_enrollment_request(student: EnrollmentModel, db: Session = Depends(get_db)):
    return HTTPException(status_code=501, detail="Not implemented")

@router.get("/", response_model=List[EnrollmentModel])
def read_enrollments_request(db: Session = Depends(get_db)):
    return HTTPException(status_code=501, detail="Not implemented")

@router.get("/{student_id}", response_model=EnrollmentModel)
def read_student_enrollments_request(course_id: str, db: Session = Depends(get_db)):
    return HTTPException(status_code=501, detail="Not implemented")
