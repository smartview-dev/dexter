from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modules.users.v1.routes import router as v1_user_router

origins = [
    "dexter.smartview.dev",
    "http://localhost:4200",
]


app = FastAPI(
    title="API dexter",
    description="API to manage chatbots",
    version="0.1.0",
    openapi_tags=[
        {"name": "v1", "description": "Version 1 of the API"},
        {"name": "users", "description": "User management"},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_user_router)
