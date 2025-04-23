from fastapi import HTTPException, status
from sqlmodel import Session, select

from core.security import Security
from modules.users.v1 import UserModel, UserRead


class AuthService:

    @staticmethod
    def login(session: Session, email: str, password: str) -> UserRead:
        query = select(UserModel).where(UserModel.email == email)
        db_user = session.exec(query).first()

        if not db_user or not Security.verify_password(password, db_user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        return UserRead.model_validate(db_user)
