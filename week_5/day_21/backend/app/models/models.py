from sqlalchemy import Column, DateTime, Integer, String, func, Text

from app.database.base import Base


class Employee(Base):
    __tablename__ = "employee"

    emp_id = Column(Integer, primary_key=True, index=True)
    emp_name = Column(String(100), nullable=False)
    designation = Column(String(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


