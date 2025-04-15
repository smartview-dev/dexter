from fastapi import HTTPException, status
from sqlmodel import Session, select
from .models import UserModel
from .schemes import UserCreate, UserRead


class UserService:
    @staticmethod
    def get_user_by_email(session: Session, email: str) -> UserRead:
        query = select(UserModel).where(UserModel.email == email)
        user = session.exec(query).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return UserRead.model_validate(user)


    @staticmethod
    def create_user(session: Session, user: UserCreate) -> UserRead:
        query = select(UserModel).where(UserModel.email == user.email)
        db_user = session.exec(query).first()

        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists"
            )

        new_user = UserModel(**user.model_dump())
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return UserRead.model_validate(new_user)
