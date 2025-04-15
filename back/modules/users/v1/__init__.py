from .models import UserModel
from .routes import router as v1_user_router
from .services import UserService
from .schemes import UserCreate, UserRead


__all__ = [
    "UserModel",
    "UserCreate",
    "UserRead",
    "v1_user_router",
    "UserService"
]
__version__ = "1.0.0"
__author__ = "Yerson Alexander Arredondo García"
__description__ = "User module for the API"
__title__ = "core"
