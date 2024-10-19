from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.database.database import get_db
from backend.api.models.enrollments import EnrollmentModel, EnrollmentModelDB
from backend.api.services.courses_services import get_course
from backend.api.services.students_services import get_student
from backend.api.services.enrollments_services import create_enrollment, get_enrollments, get_student_enrollments, \
    verify_enrollment_existence

router = APIRouter()

@router.post("/", response_model=EnrollmentModel, summary="Create a new enrollment", description="Create a new enrollment", response_description="Enrollment created", status_code=201, responses={400: {"description": "Bad request"}})
def create_enrollment_request(enrollment: EnrollmentModel, db: Session = Depends(get_db)):
    try:
        # Verify if student exist
        try:
            if get_student(enrollment.student_id, db):
                pass
            else:
                raise HTTPException(status_code=400, detail="Student not found")
        except HTTPException as e:
            raise e
        except Exception as e:
            raise e

        # Verify if course exist
        try:
            if get_course(enrollment.course_id, db):
                pass
            else:
                raise HTTPException(status_code=400, detail="Student not found")
        except HTTPException as e:
            raise e
        except Exception as e:
            raise e

        # Verify if enrollment already exist
        if verify_enrollment_existence(enrollment, db):
            raise HTTPException(status_code=400, detail="Enrollment already exist")
        # Create enrollment
        result = create_enrollment(enrollment, db)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise e

@router.get("/", response_model=List[EnrollmentModel], summary="Get all enrollments", description="Get all enrollments", response_description="Enrollments retrieved", status_code=200, responses={404: {"description": "Enrollments not found"}, 400: {"description": "Bad request"}})
def read_enrollments_request(db: Session = Depends(get_db)):
    try:
        result = get_enrollments(db)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise e

@router.get("/{student_id}", response_model=List[EnrollmentModel], summary="Get student enrollments", description="Get student enrollments", response_description="Student enrollments retrieved", status_code=200, responses={404: {"description": "Student's enrollments not found"}, 400: {"description": "Bad request"}})
def read_student_enrollments_request(student_id: int, db: Session = Depends(get_db)):
    try:
        # Verify if student exist
        try:
            if get_student(student_id, db):
                pass
            else:
                raise HTTPException(status_code=400, detail="Student not found")
        except HTTPException as e:
            raise e
        except Exception as e:
            raise e

        result = get_student_enrollments(student_id, db)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise e
