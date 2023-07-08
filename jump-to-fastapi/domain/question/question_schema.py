import datetime

from pydantic import BaseModel, validator

from domain.answer.answer_schema import Answer


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = [] # Answer 스키마로 구성된 리스트

    class Config:
        orm_mode = True


class QuestionCreate(BaseModel):
    subject: str
    content: str
    
    @validator('content')
    def not_empty(cls, v): # 빈 문자열을 허용하지 않도록 하는 어노테이션 함수
        if not v or not v.strip(): # 값이 없거나 공백인 경우
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v