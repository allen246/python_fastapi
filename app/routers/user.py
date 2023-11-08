from fastapi import APIRouter, Depends
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from fastapi import Request
from typing import List
router = APIRouter()


@router.get('/me', response_model=schemas.UserResponse)
def get_me(request: Request, db: Session = Depends(get_db), user_id: str = Depends(oauth2.require_user)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    setattr(user, 'profile_url', f"{request.base_url}api/image/download/{user.profile_id}")
    del user.profile_id
    return user

@router.get('/all', response_model=List[schemas.AllUserResponse])
def get_all(request: Request, db: Session = Depends(get_db), verified: str = Depends(oauth2.require_user)):
    response = {}
    users = db.query(models.User).all()
    return users

@router.get('/{user_id}', response_model=schemas.UserResponse)
def get_user(user_id: str, request: Request, db: Session = Depends(get_db), verified: str = Depends(oauth2.require_user)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    
    setattr(user, 'profile_url', f"{request.base_url}api/image/download/{user.profile_id}")
    del user.profile_id
    return user

