from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    course = Column(Integer, nullable=False)

    scores = relationship("Score", back_populates="student")


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    score = Column(Integer)
    student_id = Column(Integer, ForeignKey("students.id"))

    student = relationship("Student", back_populates="scores")
