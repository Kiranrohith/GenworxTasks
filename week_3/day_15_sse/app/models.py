from sqlalchemy.orm import declarative_base
from sqlalchemy import Boolean, Column, Integer, String, DateTime, func

Base = declarative_base()

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now()) 