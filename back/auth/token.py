from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

from .schemes import TokenData
from .security import Security


oauth2_token = HTTPBearer(auto_error=False)


class Token:
    @staticmethod
    def validate(token: Annotated[str, Depends(oauth2_token)]) -> TokenData:
        """
        Validate the given token.
        """
        if not token:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
                headers={"Authenticate": "Bearer"},
            )

        return Security.decode_token(token.credentials)
