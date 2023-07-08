import datetime

from pydantic import BaseModel

from domain.answer.answer_schema import Answer


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = [] # Answer 스키마로 구성된 리스트

    class Config:
        orm_mode = True