from typing import Optional

from pydantic import BaseModel, Field


class ScoreBase(BaseModel):
    score: int
    student_id: int
    subject:  Optional[str] = Field(None, description="Название предмета")


class ScoreCreate(ScoreBase):
    pass


class Score(ScoreBase):
    id: int
    subject: str

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    name: str
    age: int
    course: int


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int
    scores: list[Score] = []

    class Config:
        orm_mode = True