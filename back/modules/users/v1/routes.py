from fastapi import APIRouter, Depends
from sqlmodel import Session
from core import get_session
from .services import UserService
from .schemes import UserCreate, UserRead


router = APIRouter(prefix="/v1/users", tags=["v1", "users"])

@router.get("/users/{email}", response_model=UserRead)
def get_user_profile(
    email: str,
    session: Session = Depends(get_session)
):
    user = UserService.get_user_by_email(session, email)
    return user


@router.post("/users", response_model=UserRead)
def create_user(
    user: UserCreate,
    session: Session = Depends(get_session),
):
    user = UserService.create_user(session, user)
    return user
