from sqlalchemy.orm.session import Session
from schemas.response import ResponseBase
from models.models import DbResponse
from fastapi import HTTPException, status
from datetime import datetime

def add_response(db: Session, request: ResponseBase):
    new_response = DbResponse(
        text = request.text,
        username = request.username,
        comment_id = request.comment_id,
        timestamp = datetime.now()
    )
    db.add(new_response)
    db.commit()
    db.refresh(new_response)
    return new_response

def update_response(db:Session, id: int, request: ResponseBase):
    response = db.query(DbResponse).filter(DbResponse.id == id)
    if not response.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail='Esa respuesta no existe'
                            )
    response.update({
        DbResponse.text: request.text,
        DbResponse.edited: True
    })
    db.commit()
    return 'Respuesta actualizada'

def delete_response(db: Session, id: int):
    response = db.query(DbResponse).filter(DbResponse.id == id)
    if not response.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail='Esa respuesta no existe'
                            )
    db.delete(response)
    db.commit()
    return 'Respuesta eliminada'