from fastapi import FastAPI
from modules.users.v1.routes import router as v1_user_router


app = FastAPI(
    title="API dexter",
    description="API para gestionar chatbots",
    version="0.1.0",
    openapi_tags=[
        {"name": "v1", "description": "Version 1 del API"},
        {"name": "users", "description": "Gestión de usuarios"},
    ],
)

app.include_router(v1_user_router)
