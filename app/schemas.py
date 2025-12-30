from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    duration: Optional[str] = None
    lectures: Optional[int] = 0
    assignments: Optional[int] = 0
    rating: Optional[float] = 0.0
    instructor: Optional[str] = None
    udemy_link: str
    tags: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    slug: str
    created_at: datetime

    class Config:
        from_attributes = True
