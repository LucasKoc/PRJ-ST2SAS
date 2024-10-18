from fastapi import HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

from backend.api.core.settings import Settings  # Adjusted import based on your project structure

# Base class for SQLAlchemy models
Base = declarative_base()

# Initialize engine and SessionLocal to None
engine = None
SessionLocal = None


def create_database_if_not_exists():
    # Connect to the PostgreSQL server (excluding the database name)
    root_engine = create_engine(Settings.DATABASE_URL_NO_DB)

    try:
        # Check if the database exists
        with root_engine.connect() as conn:
            # Set autocommit mode for this connection
            conn = conn.execution_options(isolation_level="AUTOCOMMIT")
            result = conn.execute(
                text(f"SELECT 1 FROM pg_database WHERE datname='{Settings.POSTGRES_DB}'")
            )
            exists = result.scalar() is not None
            if not exists:
                conn.execute(
                    text(f"CREATE DATABASE {Settings.POSTGRES_DB};")
                )
                print(f"Database {Settings.POSTGRES_DB} created")
    except:
        pass

    # Reconnect to the newly created or existing database
    global engine
    engine = create_engine(Settings.DATABASE_FULL_URL)

    # Check if the schema exists
    with engine.connect() as conn:
        # Set autocommit mode for this connection
        conn = conn.execution_options(isolation_level="AUTOCOMMIT")
        result = conn.execute(
            text(f"SELECT 1 FROM information_schema.schemata WHERE schema_name='{Settings.POSTGRES_SCHEMA}';")
        )
        exists = result.scalar() is not None
        if not exists:
            conn.execute(
                text(f"CREATE SCHEMA {Settings.POSTGRES_SCHEMA};")
            )
            print(f"Schema {Settings.POSTGRES_SCHEMA} created")


    # Now that the database exists, initialize SessionLocal
    global SessionLocal
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return engine


def get_db():
    if SessionLocal is None:
        raise HTTPException(status_code=500, detail="Database session not initialized.")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
