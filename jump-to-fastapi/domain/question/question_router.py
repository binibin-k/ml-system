from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema, question_crud

router = APIRouter(
    prefix="/api/question", # 요청 URL에 항상 포함되어야 하는 값
)

@router.get("/list", response_model=list[question_schema.Question])
def question_list(db:Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list