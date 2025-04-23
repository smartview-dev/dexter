from datetime import datetime, timezone
from sqlmodel import Field
from core import BaseModel


class TokenModel(BaseModel, table=True):
    payload: str
    expires_at: datetime
    created_at: datetime = Field(default=datetime.now(timezone.utc))

    __tablename__ = "token"


class RefreshTokenModel(BaseModel, table=True):
    payload: str
    expires_at: datetime
    revoked: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now(timezone.utc))

    __tablename__ = "refresh_token"
