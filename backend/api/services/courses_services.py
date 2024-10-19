from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.api.models.courses import CourseModel, CourseModelDB

def coursemodel_to_coursemodeldb(course: CourseModel) -> CourseModelDB:
    return CourseModelDB(
        course_id=course.course_id,
        course_name=course.course_name,
        teacher_id=course.teacher_id,
        picture_path=course.picture_path
    )

def coursemodeldb_to_coursemodel(course: CourseModelDB) -> CourseModel:
    return CourseModel(
        course_id=course.course_id,
        course_name=course.course_name,
        teacher_id=course.teacher_id,
        picture_path=course.picture_path
    )

def create_course(course: CourseModel, db: Session) -> CourseModel:
    db_course = coursemodel_to_coursemodeldb(course)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return coursemodeldb_to_coursemodel(db_course)

def get_courses(db: Session) -> List[CourseModel]:
    courses = db.query(CourseModelDB).all()
    return [coursemodeldb_to_coursemodel(course) for course in courses]

def get_course(course_id: str, db: Session) -> CourseModel:
    course = db.query(CourseModelDB).filter(CourseModelDB.course_id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return coursemodeldb_to_coursemodel(course)
