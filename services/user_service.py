from sqlalchemy.orm import Session
from app.domain.user_model import UserCreate
from app.repository.user_repository import create_user, get_user_by_id, get_all_users

def create_user_service(db: Session, user: UserCreate):
    if len(user.name) < 2:
        raise ValueError("El nombre debe tener al menos 2 caracteres")
    return create_user(db, user.name, user.email)

def get_user_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError("Usuario no encontrado")
    return user

def get_all_users_service(db: Session):
    return get_all_users(db)
