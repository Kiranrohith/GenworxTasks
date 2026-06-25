from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:Kiran246@localhost:5432/advance_db"

try:
    engine = create_engine(DATABASE_URL, echo=False)
    SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
except SQLAlchemyError as exc:
    raise RuntimeError(f"Failed to initialize database engine: {exc}") from exc


def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as exc:
        db.rollback()
        raise RuntimeError(f"Database session error: {exc}") from exc
    finally:
        db.close()

