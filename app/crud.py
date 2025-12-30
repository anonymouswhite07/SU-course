from sqlalchemy.orm import Session
from . import models, schemas
from slugify import slugify
import uuid

def get_course(db: Session, slug: str):
    return db.query(models.Course).filter(models.Course.slug == slug).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).order_by(models.Course.created_at.desc()).offset(skip).limit(limit).all()

def create_course(db: Session, course: schemas.CourseCreate):
    base_slug = slugify(course.title)
    slug = base_slug
    
    # Simple uniqueness check
    counter = 1
    while db.query(models.Course).filter(models.Course.slug == slug).first():
        slug = f"{base_slug}-{counter}"
        counter += 1
        
    db_course = models.Course(**course.dict(), slug=slug)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
