from fastapi import APIRouter, Depends
from sqlmodel import Session

from core import get_session, TokenData, TokenValidator
from .services import UserService
from .schemes import UserCreate, UserRead


router = APIRouter(
    dependencies=[Depends(get_session), Depends(TokenValidator.access)],
    prefix="/v1/users",
    tags=["v1", "users"],
)

db_session = router.dependencies[0]
token_access = router.dependencies[1]


@router.get("/me", response_model=UserRead)
def get_user(
    session: Session = db_session,
    token: TokenData = token_access,
):
    user = UserService.get_by_email(session, token.email)
    return user


@router.get("/{email}", response_model=UserRead)
def get_users(
    email: str,
    session: Session = db_session,
):
    user = UserService.get_by_email(session, email)
    return user


@router.post("", response_model=UserRead)
def create_user(
    user: UserCreate,
    session: Session = db_session,
):
    user = UserService.create(session, user)
    return user
