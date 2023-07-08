import datetime

from pydantic import BaseModel, validator


class AnswerCreate(BaseModel):
    content: str

    @validator('content')
    def not_empty(cls, v): # 빈 문자열을 허용하지 않도록 하는 어노테이션 함수
        if not v or not v.strip(): # 값이 없거나 공백인 경우
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class Answer(BaseModel): # 단 한 건에 대한 스키마
    id: int
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True

