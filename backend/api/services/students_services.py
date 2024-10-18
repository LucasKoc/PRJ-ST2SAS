from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.api.models.students import StudentModel, StudentModelDB


def studentmodel_to_studentmodeldb(student: StudentModel) -> StudentModelDB:
    return StudentModelDB(
        student_id=student.student_id,
        first_name=student.first_name,
        last_name=student.last_name,
        school_email=student.school_email,
        phone=student.phone,
        picture_path=student.picture_path
    )


def studentmodeldb_to_studentmodel(student: StudentModelDB) -> StudentModel:
    return StudentModel(
        student_id=student.student_id,
        first_name=student.first_name,
        last_name=student.last_name,
        school_email=student.school_email,
        phone=student.phone,
        picture_path=student.picture_path
    )


def create_student(student: StudentModel, db: Session) -> StudentModel:
    db_student = studentmodel_to_studentmodeldb(student)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return studentmodeldb_to_studentmodel(db_student)

def get_students(db: Session) -> List[StudentModel]:
    query = db.query(StudentModelDB).all()
    return [studentmodeldb_to_studentmodel(student) for student in query]

def get_student(student_id: int, db: Session) -> StudentModel:
    query = db.query(StudentModelDB).filter(StudentModelDB.student_id == student_id).first()
    if query is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return studentmodeldb_to_studentmodel(query)

