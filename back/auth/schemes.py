from typing import Optional
from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    expires_in: int
    token: str
    token_type: str = "Bearer"
    refresh_token: str


class TokenData(BaseModel):
    email: EmailStr
    exp: int
    iat: int
    sub: str
    type: Optional[str] = "access"
