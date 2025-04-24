from .base_model import BaseModel
from .bot import Bot
from .config import settings
from .custom_pg_vector import CustomPGVector
from .database import get_session
from .schemes import Token, TokenData
from .security import Security
from .token import Token as TokenValidator


__all__ = [
    "BaseModel",
    "Bot",
    "CustomPGVector",
    "get_session",
    "settings",
    "Security",
    "Token",
    "TokenData",
    "TokenValidator",
]
__version__ = "1.0.0"
__author__ = "Yerson Alexander Arredondo García"
__description__ = "Core module for the API"
__title__ = "core"
