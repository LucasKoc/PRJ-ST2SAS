from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import backend.api.database.database as db
from backend.api.database.init_data import init_data
from backend.api.core.settings import Settings

from backend.api.routes.students_route import router as students_router
from backend.api.routes.teachers_route import router as teachers_router
from backend.api.routes.courses_route import router as courses_router
from backend.api.routes.enrollments_route import router as enrollments_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the car routes
app.include_router(students_router, prefix="/students", tags=["students"])
app.include_router(teachers_router, prefix="/teachers", tags=["teachers"])
app.include_router(courses_router, prefix="/courses", tags=["courses"])
app.include_router(enrollments_router, prefix="/enrollments", tags=["enrollments"])

@app.get("/")
def read_root():
    return {"message": "Routes available at /docs"}

@app.on_event("startup")
def on_startup():
    # Create the database if it doesn't exist and get the engine
    engine = db.create_database_if_not_exists()

    # Create all tables in the database if they don't exist
    db.Base.metadata.create_all(bind=engine)

    # Insert mockup data in database if table created before
    try:
        session = db.SessionLocal()
        init_data(session)
        session.close()
    except Exception as e:
        print("Error occurred during data initialization: ", str(e))

if __name__ == "__main__":
    uvicorn.run("backend.api.main:app", host=Settings.API_HOST, port=int(Settings.API_PORT), reload=True, log_level="info")