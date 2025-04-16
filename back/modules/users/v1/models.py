from datetime import datetime, timezone
from typing import Optional
from pydantic import EmailStr
from sqlmodel import Field
from core import BaseModel


class UserModel(BaseModel, table=True):
    first_name: str
    last_name: str
    email: EmailStr = Field(index=True, unique=True)
    password: str
    is_active: bool = True
    created_at: datetime = Field(default=datetime.now(timezone.utc))
    updated_at: Optional[datetime] = Field(default=datetime.now(timezone.utc))

    __tablename__ = "user"
