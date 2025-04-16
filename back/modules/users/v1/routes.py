from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials
from sqlmodel import Session

from auth import Security, Token, TokenData, TokenValidator
from core import get_session
from .services import UserService
from .schemes import UserCreate, UserRead


router = APIRouter(
    dependencies=[Depends(get_session)],
    prefix="/v1/users",
    tags=["v1", "users"],
)

db_session = router.dependencies[0]


@router.get("", response_model=UserRead)
def get_user(
    session: Session = db_session,
    token: TokenData = Depends(TokenValidator.validate),
):
    user = UserService.get_by_email(session, token.email)
    return user


@router.get("/{email}", response_model=UserRead)
def get_users(
    email: str,
    session: Session = db_session,
    _=Depends(TokenValidator.validate),
):
    user = UserService.get_by_email(session, email)
    return user


@router.post("", response_model=UserRead)
def create_user(
    user: UserCreate,
    session: Session = db_session,
    _=Depends(TokenValidator.validate),
):
    user = UserService.create(session, user)
    return user


@router.post("/login", response_model=Token)
def login_user(
    form_data: Annotated[HTTPBasicCredentials, Depends()],
    session: Session = db_session,
):
    user = UserService.login(session, form_data.username, form_data.password)
    return Security.generate_tokens(user)
