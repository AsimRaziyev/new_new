from sqlalchemy.orm import Session

import models
import schemas


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Student).offset(skip).limit(limit).all()


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name, age=student.age, course=student.course)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = get_student(db, student_id)
    if db_student:
        db_student.name = student.name
        db_student.age = student.age
        db_student.course = student.course
        db.commit()
        db.refresh(db_student)
    return db_student


def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student


def get_score(db: Session, score_id: int):
    return db.query(models.Score).filter(models.Score.id == score_id).first()


def create_score(db: Session, score: schemas.ScoreCreate):
    db_score = models.Score(**score.dict())
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score


def update_score(db: Session, score_id: int, score: schemas.ScoreCreate):
    db_score = get_score(db, score_id)
    if db_score:
        db_score.score = score.score
        db_score.subject = score.subject
        db.commit()
        db.refresh(db_score)
    return db_score


def delete_score(db: Session, score_id: int):
    db_score = get_score(db, score_id)
    if db_score:
        db.delete(db_score)
        db.commit()
    return db_score