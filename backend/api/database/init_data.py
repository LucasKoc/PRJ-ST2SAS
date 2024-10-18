from sqlalchemy.orm import Session
from sqlalchemy.sql.coercions import expect

from backend.api.models.courses import CourseModelDB
from backend.api.models.enrollments import EnrollmentModelDB
from backend.api.models.students import StudentModelDB
from backend.api.models.teachers import TeacherModelDB

def init_data(db: Session):
    """
    This function is used to initialize the database with some mockup data.
    Execute this function if the database is empty.
    :param db: SQLAlchemy Session
    :return: None
    """
    mockup_data = {
        "students": {
            "data": [
                {
                    "student_id": 20210615,
                    "first_name": "Lucas",
                    "last_name": "KOCOGLU",
                    "school_email": "lucas.kocoglu@efrei.net",
                    "phone": "0767899931",
                    "picture_path": None
                },
                {
                    "student_id": 20210527,
                    "first_name": "Maxime",
                    "last_name": "BOULLE",
                    "school_email": "maxime.boulle@efrei.net",
                    "phone": None,
                    "picture_path": None
                },
                {
                    "student_id": 20210619,
                    "first_name": "Nicolas",
                    "last_name": "LAHIMASY",
                    "school_email": "nicolas.lahimasy@efrei.net",
                    "phone": None,
                    "picture_path": None
                }
            ]
        },
        "teachers": {
            "data": [
                {
                    "professor_id": "ijenhani",
                    "first_name": "Ilyes",
                    "last_name": "JENHANI",
                    "school_email": "ilyes.jenhani@efrei.fr",
                    "phone": None,
                    "specialty": "Software Engineering Responsible",
                    "picture_path": None
                },
                {
                    "professor_id": "yaitelmahjoub",
                    "first_name": "Youssef",
                    "last_name": "AIT EL MAHJOUB",
                    "school_email": "youssef.ait-el-mahjoub@efrei.fr",
                    "phone": "0616591379",
                    "specialty": "IT Paris & LSI BDX. Responsible, Researcher-Teacher",
                    "picture_path": None
                }
            ]
        },
        "courses": {
            "data": [
                {
                    "course_id": "ST2SAS",
                    "course_name": "Docker Containers",
                    "professor_id": "ijenhani",
                    "picture_url": None
                },
                {
                    "course_id": "ST2AIM",
                    "course_name": "AI & Machine Learning for IT Engineer",
                    "professor_id": "yaitelmahjoub",
                    "picture_url": None
                }
            ]
        },
        "enrollments": {
            "data": [
                {"student_id": 20210615, "course_id": "ST2SAS", "grade": None},
                {"student_id": 20210527, "course_id": "ST2SAS", "grade": None},
                {"student_id": 20210619, "course_id": "ST2SAS", "grade": None},
                {"student_id": 20210615, "course_id": "ST2AIM", "grade": None},
                {"student_id": 20210527, "course_id": "ST2AIM", "grade": None},
                {"student_id": 20210619, "course_id": "ST2AIM", "grade": None}
            ]
        }
    }

    try:
        if (db.query(CourseModelDB).count() > 0) or (db.query(EnrollmentModelDB).count() > 0) or (db.query(StudentModelDB).count() > 0) or (db.query(TeacherModelDB).count() > 0):
            print(db.query(CourseModelDB).count(), db.query(EnrollmentModelDB).count(), db.query(StudentModelDB).count(), db.query(TeacherModelDB).count())
            return
    except Exception as e:
        pass


    for student in mockup_data["students"]["data"]:
        student = StudentModelDB(
            student_id=student["student_id"],
            first_name=student["first_name"],
            last_name=student["last_name"],
            school_email=student["school_email"],
            phone=student["phone"],
            picture_path=student["picture_path"]
        )
        db.add(student)
    db.commit()

    for teacher in mockup_data["teachers"]["data"]:
        teacher = TeacherModelDB(
            teacher_id=teacher["professor_id"],
            first_name=teacher["first_name"],
            last_name=teacher["last_name"],
            school_email=teacher["school_email"],
            phone=teacher["phone"],
            speciality=teacher["specialty"],
            picture_path=teacher["picture_path"]
        )
        db.add(teacher)
    db.commit()

    for course in mockup_data["courses"]["data"]:
        course = CourseModelDB(
            course_id=course["course_id"],
            course_name=course["course_name"],
            teacher_id=course["professor_id"],
            picture_path=course["picture_url"]
        )
        db.add(course)
    db.commit()

    for enrollment in mockup_data["enrollments"]["data"]:
        enrollment = EnrollmentModelDB(
            student_id=enrollment["student_id"],
            course_id=enrollment["course_id"],
            grade=enrollment["grade"]
        )
        db.add(enrollment)
    db.commit()
