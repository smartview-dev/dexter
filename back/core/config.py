from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_ALGORITHM: str
    JWT_SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
