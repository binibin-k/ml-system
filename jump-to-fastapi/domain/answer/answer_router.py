from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.answer import answer_schema, answer_crud
from domain.question import question_crud

router = APIRouter(
    prefix="/api/answer",
)


@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT) # 리턴할 응답이 없으므로 응답없음 코드를 리턴
def answer_create(question_id: int, _answer_create: answer_schema.AnswerCreate, db: Session = Depends(get_db)):
    
    # create answer
    question = question_crud.get_question(db, question_id=question_id)
    if not question: # question이 없는 경우
        raise HTTPException(status_code=404, detail="Question not found")
    answer_crud.create_answer(db, question=question, answer_create=_answer_create)