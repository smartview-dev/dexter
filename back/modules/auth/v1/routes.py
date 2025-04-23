from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials
from sqlmodel import Session

from core import get_session, Security, Token
from .services import AuthService


router = APIRouter(
    dependencies=[Depends(get_session)],
    prefix="/v1/auth",
    tags=["v1", "auth"],
)

db_session = router.dependencies[0]


@router.post("/login", response_model=Token)
def login_user(
    form_data: Annotated[HTTPBasicCredentials, Depends()],
    session: Session = db_session,
):
    user = AuthService.login(session, form_data.username, form_data.password)
    return Security.generate_tokens(user)
