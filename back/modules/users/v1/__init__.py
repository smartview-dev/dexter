from .models import UserModel
from .routes import router
from .schemes import UserCreate, UserRead
from .services import UserService

__all__ = [
    "UserModel",
    "router",
    "UserCreate",
    "UserRead",
    "UserService",
]


__version__ = "1.0.0"
__author__ = "Yerson Alexander Arredondo García"
__description__ = "Users module"
__title__ = "users"
