import bcrypt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status
from jose import JWTError, jwt

from core import settings
from .schemes import Token, TokenData


class Security:
    @staticmethod
    def _decode_token(token: str) -> TokenData:
        """
        Decode and validate the given JWT token.
        If the token has expired or is invalid, an HTTP 401 error is raised.
        """
        try:
            payload = jwt.decode(
                token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
            )
            now = int(datetime.now(timezone.utc).timestamp())
            if payload.get("exp", 0) < now:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token expired",
                    headers={"Authenticate": "Bearer"},
                )
            return TokenData(**payload)
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"Authenticate": "Bearer"},
            )

    @staticmethod
    def _generate_payload(
        user: "UserRead", exp_delta: timedelta, token_type: str
    ) -> dict:
        """
        Generate the payload for a token for the given user, expiration timedelta, and token type.
        """
        now = datetime.now(timezone.utc)
        return {
            "email": user.email,
            "iat": int(now.timestamp()),
            "exp": int((now + exp_delta).timestamp()),
            "sub": str(user.id),
            "type": token_type,
        }

    @staticmethod
    def _sign_token(payload: dict) -> str:
        """
        Sign and encode the JWT token using the defined configuration.
        """
        headers = {"alg": settings.JWT_ALGORITHM, "typ": "JWT"}
        return jwt.encode(
            payload,
            settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM,
            headers=headers,
        )

    @staticmethod
    def generate_tokens(user: "UserRead") -> Token:
        """
        Generate both access and refresh tokens for the given user.
        """
        access_payload = Security._generate_payload(
            user,
            timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES),
            "access",
        )
        refresh_payload = Security._generate_payload(
            user,
            timedelta(days=settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS),
            "refresh",
        )
        return Token(
            expires_in=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            token=Security._sign_token(access_payload),
            refresh_token=Security._sign_token(refresh_payload),
        )

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash the given password using bcrypt.
        """
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed.decode("utf-8")

    @staticmethod
    def validate_access_token(token: str) -> TokenData:
        """
        Validates that the provided token is an access token.
        If not, raises a 401 Unauthorized error.
        """
        token_data = Security._decode_token(token)
        if token_data.type != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The provided token is not an access token",
                headers={"Authenticate": "Bearer"},
            )
        return token_data

    @staticmethod
    def validate_refresh_token(token: str) -> TokenData:
        """
        Validates that the provided token is a refresh token.
        If not, raises a 401 Unauthorized error.
        """
        token_data = Security._decode_token(token)
        if token_data.type != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The provided token is not a refresh token",
                headers={"Authenticate": "Bearer"},
            )
        return token_data

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verify that the given plain password matches the hashed password.
        """
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), hashed_password.encode("utf-8")
        )
