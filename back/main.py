from fastapi import FastAPI
from modules.users.v1.routes import router as v1_user_router


app = FastAPI(
    title="API dexter",
    description="API to manage chatbots",
    version="0.1.0",
    openapi_tags=[
        {"name": "v1", "description": "Version 1 of the API"},
        {"name": "users", "description": "User management"},
    ],
)

app.include_router(v1_user_router)
