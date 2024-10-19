from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.database.database import get_db
from backend.api.models.teachers import TeacherModel
from backend.api.models.errors import ErrorResponse
from backend.api.services.teachers_services import create_teacher, get_teacher, get_teachers

router = APIRouter()

@router.post("/", response_model=TeacherModel, responses={400: {"model": ErrorResponse, "description": "Bad request"}}, status_code=201)
def create_teacher_request(teacher: TeacherModel, db: Session = Depends(get_db)):
    """
    Create a new teacher
    """
    try:
        try:
            if get_teacher(teacher.teacher_id, db):
                raise HTTPException(status_code=400, detail="Teacher already registered")
        except HTTPException as e:
            if e.status_code == 404:
                pass
            else:
                raise e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        result = create_teacher(teacher, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[TeacherModel], summary="Get all teachers", description="Get all teachers", responses={400: {"model": ErrorResponse, "description": "Bad request"}}, status_code=200)
def read_teachers_request(db: Session = Depends(get_db)):
    try:
        result = get_teachers(db)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{teacher_id}", response_model=TeacherModel, summary="Get a specified teacher", description="Get a specified teacher", responses={404: {"model": ErrorResponse, "description": "Teacher not found"}, 400: {"model": ErrorResponse, "description": "Bad request"}}, status_code=200)
def read_teacher_request(teacher_id: str, db: Session = Depends(get_db)):
    try:
        result = get_teacher(teacher_id, db)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
