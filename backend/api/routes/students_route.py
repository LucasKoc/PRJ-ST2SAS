from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from backend.api.database.database import get_db
from backend.api.models.errors import ErrorResponse
from backend.api.models.students import StudentModel
from backend.api.services.students_services import create_student, get_students, get_student

router = APIRouter()

@router.post("/", response_model=StudentModel, summary="Create a new student", description="Create a new student", response_description="The student data", status_code=201)
def create_student_request(student: StudentModel, db: Session = Depends(get_db), response: Response = None):
    """
    Create a new student
    """
    try:
        try:
            if get_student(student.student_id, db):
                raise HTTPException(status_code=400, detail="Student already registered")
        except HTTPException as e:
            if e.status_code == 404:
                pass
            else:
                raise e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        result = create_student(student, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[StudentModel], summary="Get all students", description="Get all students", response_description="List of students", status_code=200, responses={400: {"model": ErrorResponse, "description": "Bad request"}})
def read_students_request(db: Session = Depends(get_db)):
    try:
        result = get_students(db)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{student_id}", response_model=StudentModel, summary="Get a specific student", description="Get a specific student", response_description="The requested student data", status_code=200, responses={404: {"model": ErrorResponse, "description": "Student not found"}, 400: {"model": ErrorResponse, "description": "Bad request"}})
def read_student_request(student_id: int, db: Session = Depends(get_db)):
    try:
        result = get_student(student_id, db)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
