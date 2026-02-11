from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models.user import User
from app.db.session import get_db
from app.core.security import hash_password

router = APIRouter()

@router.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Here you would typically add logic to save the user to a database
    db_user = User(**user.dict(
        email=user.email,
        username=user.username,
        password_hash=hash_password(user.password)
    ))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": f"User {db_user.username} registered successfully!"}