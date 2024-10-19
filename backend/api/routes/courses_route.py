from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.database.database import get_db
from backend.api.models.courses import CourseModel
from backend.api.models.errors import ErrorResponse
from backend.api.services.courses_services import create_course, get_course, get_courses
from backend.api.services.teachers_services import get_teacher

router = APIRouter()

@router.post("/", response_model=CourseModel, responses={400: {"model": ErrorResponse, "description": "Bad request"}}, status_code=201)
def create_course_request(course: CourseModel, db: Session = Depends(get_db)):
    """
    Create a new course
    """
    try:
        # Verify if the course is already registered
        try:
            if get_course(course.course_id, db):
                raise HTTPException(status_code=400, detail="Course already registered")
        except HTTPException as e:
            if e.status_code == 404:
                pass
            else:
                raise e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

        try:
            # If teacher exist, create the course
            if get_teacher(course.teacher_id, db):
                result = create_course(course, db)
                return result
            else:
                raise HTTPException(status_code=400, detail="Teacher not found")
        except HTTPException as e:
            if e.status_code == 404:
                raise HTTPException(status_code=400, detail="Teacher not found")
            else:
                raise e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[CourseModel], summary="Get all courses", description="Get all courses", responses={400: {"model": ErrorResponse, "description": "Bad request"}}, status_code=200)
def read_courses_request(db: Session = Depends(get_db)):
    try:
        result = get_courses(db)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{course_id}", response_model=CourseModel, summary="Get a specified course", description="Get a specified course", responses={404: {"model": ErrorResponse, "description": "Course not found"}, 400: {"model": ErrorResponse, "description": "Bad request"}}, status_code=200)
def read_course_request(course_id: str, db: Session = Depends(get_db)):
    try:
        result = get_course(course_id, db)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))