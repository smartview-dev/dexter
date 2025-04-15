from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str

    class Config:
        from_attributes = True


class UserRead(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
