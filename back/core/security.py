# from datetime import datetime, timedelta
# from typing import Annotated, Optional
# from fastapi import Depends, HTTPException, status
# from fastapi.security import HTTPBearer
# from jose import JWTError, jwt
# from sqlmodel import Session

# from .config import settings
# from .database import get_session
# # Remove this line:
# # from modules.users.v1 import PermissionService, User, UserService

# oauth2_token = HTTPBearer(auto_error=False)

# async def get_current_user(
#     token: str = Depends(oauth2_token),
#     session: Session = Depends(get_session)
# ):
#     from modules.users.v1 import UserService, User  # Lazy import
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(
#             token,
#             settings.SECRET_KEY,
#             algorithms=[settings.ALGORITHM]
#         )
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception

#     user = UserService.get_user_with_permissions(session, username)
#     if user is None:
#         raise credentials_exception

#     return user

# def create_access_token(user):
#     from modules.users.v1 import PermissionService  # Lazy import
#     permissions = PermissionService.get_user_permissions(user)
#     payload = {
#         "sub": user.username,
#         "permissions": permissions,
#         "exp": datetime.now(datetime.timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     }
#     return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

# class PermissionDependency:
#     def __init__(self, required_permissions: Optional[list[str]] = None):
#         self.required_permissions = required_permissions or []

#     def __call__(self, user: Annotated["User", Depends(get_current_user)]):
#         from modules.users.v1 import PermissionService  # Lazy import
#         for perm in self.required_permissions:
#             if not PermissionService.has_permission(user, perm):
#                 raise HTTPException(
#                     status_code=status.HTTP_403_FORBIDDEN,
#                     detail=f"Requiere el permiso: {perm}"
#                 )
#         return user

# def permission_required(permission: str):
#     def dependency(current_user: Annotated["User", Depends(get_current_user)]):
#         from modules.users.v1 import PermissionService  # Lazy import
#         if not PermissionService.has_permission(current_user, permission):
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN,
#                 detail="Permisos insuficientes para realizar esta acción"
#             )
#         return current_user
#     return Depends(dependency)
