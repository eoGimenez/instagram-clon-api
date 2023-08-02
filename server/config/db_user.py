from sqlalchemy.orm.session import Session
from sqlalchemy import or_
from schemas.user import UserBase
from models.models import DbUser
from fastapi import HTTPException, status
from config.db_auth import get_password_hashed

def post_user(db: Session, request: UserBase):
    new_user = DbUser (
        username=request.username,
        email=request.email,
        password=get_password_hashed(request.password),
        active=True
    )
    user = db.query(DbUser).filter(or_(DbUser.email == request.email, DbUser.username == request.username)).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This username or email already exists.')
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(db:Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id}, not found')
    return user