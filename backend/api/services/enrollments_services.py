from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.api.models.enrollments import EnrollmentModel, EnrollmentModelDB

def enrollmentmodel_to_enrollmentmodeldb(enrollment: EnrollmentModel) -> EnrollmentModelDB:
    return EnrollmentModelDB(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        grade=enrollment.grade
    )

def enrollmentmodeldb_to_enrollmentmodel(enrollment: EnrollmentModelDB) -> EnrollmentModel:
    return EnrollmentModel(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        grade=enrollment.grade
    )

def create_enrollment(enrollment: EnrollmentModel, db: Session) -> EnrollmentModel:
    db_enrollment = enrollmentmodel_to_enrollmentmodeldb(enrollment)
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return enrollmentmodeldb_to_enrollmentmodel(db_enrollment)

def get_enrollments(db: Session) -> List[EnrollmentModel]:
    query = db.query(EnrollmentModelDB).all()
    if query is None:
        raise HTTPException(status_code=404, detail="Enrollments not found")
    return [enrollmentmodeldb_to_enrollmentmodel(enrollment) for enrollment in query]

def get_student_enrollments(student_id: int, db: Session) -> List[EnrollmentModel]:
    query = db.query(EnrollmentModelDB).filter(EnrollmentModelDB.student_id == student_id).all()
    if query is None:
        raise HTTPException(status_code=404, detail="Student's enrollments not found")
    return [enrollmentmodeldb_to_enrollmentmodel(enrollment) for enrollment in query]

def verify_enrollment_existence(enrollment: EnrollmentModel, db: Session) -> bool:
    query = db.query(EnrollmentModelDB).filter(EnrollmentModelDB.student_id == enrollment.student_id).filter(EnrollmentModelDB.course_id == enrollment.course_id).first()
    if query is None:
        return False
    return True