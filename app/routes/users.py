from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.db import SessionLocal
from app.schemas.user import User, UserCreate, UserResponse
from app.services.user import get_user, create_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    return db_user


@router.get("/{user_email}", response_model=UserResponse)
def get_user_by_email(user_email: str, db: Session = Depends(get_db)):
    user = get_user(db=db, user_email=user_email)

    return user
