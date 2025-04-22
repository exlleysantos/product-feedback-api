from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User as DBUser
from app.schemas.user import User, UserCreate


def get_user(db: Session, user_email: str):

    user = db.query(DBUser).filter(DBUser.email == user_email).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user


def create_user(db: Session, user: UserCreate):

    existing_user = db.query(DBUser).filter(DBUser.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400, detail="Já existe um usuário com esse email cadastrado!"
        )

    db_user = DBUser(name=user.name, email=user.email, password=user.password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
