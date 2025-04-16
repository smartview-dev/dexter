from fastapi import HTTPException, status
from sqlmodel import Session, select

from auth import Security
from .models import UserModel
from .schemes import UserCreate, UserRead


class UserService:
    @staticmethod
    def create(session: Session, user: UserCreate) -> UserRead:
        query = select(UserModel).where(UserModel.email == user.email)
        db_user = session.exec(query).first()

        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
            )

        new_user = UserModel(
            email=user.email,
            password=Security.hash_password(user.password),
            first_name=user.first_name,
            last_name=user.last_name,
            is_active=True,
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return UserRead.model_validate(new_user)

    @staticmethod
    def get_by_email(session: Session, email: str) -> UserRead:
        query = select(UserModel).where(UserModel.email == email)
        user = session.exec(query).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

        return UserRead.model_validate(user)

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
