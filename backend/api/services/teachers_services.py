from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.api.models.teachers import TeacherModel, TeacherModelDB


def teachertmodel_to_teachermodeldb(teacher: TeacherModel) -> TeacherModelDB:
    return TeacherModelDB(
        teacher_id=teacher.teacher_id,
        first_name=teacher.first_name,
        last_name=teacher.last_name,
        school_email=teacher.school_email,
        phone=teacher.phone,
        speciality=teacher.speciality,
        picture_path=teacher.picture_path
    )


def teachermodeldb_to_teachermodel(teacher: TeacherModelDB) -> TeacherModel:
    return TeacherModel(
        teacher_id=teacher.teacher_id,
        first_name=teacher.first_name,
        last_name=teacher.last_name,
        school_email=teacher.school_email,
        phone=teacher.phone,
        speciality=teacher.speciality,
        picture_path=teacher.picture_path
    )


def create_teacher(teacher: TeacherModel, db: Session) -> TeacherModel:
    db_teacher = teachertmodel_to_teachermodeldb(teacher)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return teachermodeldb_to_teachermodel(db_teacher)

def get_teachers(db: Session) -> List[TeacherModel]:
    query = db.query(TeacherModelDB).all()
    return [teachermodeldb_to_teachermodel(teacher) for teacher in query]

def get_teacher(teacher_id: str, db: Session) -> TeacherModel:
    query = db.query(TeacherModelDB).filter(TeacherModelDB.teacher_id == teacher_id).first()
    if query is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teachermodeldb_to_teachermodel(query)