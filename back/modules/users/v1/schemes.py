from datetime import datetime
from typing import Optional
import uuid
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str

    class Config:
        from_attributes = True


class UserRead(UserBase):
    id: uuid.UUID
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
