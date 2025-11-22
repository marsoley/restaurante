from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.user_service import (
    create_user_service, get_user_service, get_all_users_service
)
from app.domain.user_model import UserCreate, UserRead
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=UserRead)
def crear_usuario(user: UserCreate, db: Session = Depends(get_db)):
    try:
        usuario = create_user_service(db, user)
        return usuario
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserRead)
def obtener_usuario(user_id: int, db: Session = Depends(get_db)):
    try:
        return get_user_service(db, user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[UserRead])
def listar_usuarios(db: Session = Depends(get_db)):
    return get_all_users_service(db)
