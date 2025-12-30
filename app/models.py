from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from .database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    slug = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    duration = Column(String, nullable=True)
    lectures = Column(Integer, default=0)
    assignments = Column(Integer, default=0)
    rating = Column(Float, default=0.0)
    instructor = Column(String, nullable=True)
    udemy_link = Column(String, nullable=False)
    tags = Column(String, nullable=True)  # Comma-separated or JSON string
    created_at = Column(DateTime, default=datetime.utcnow)
