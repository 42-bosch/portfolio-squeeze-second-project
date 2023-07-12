from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.routes.user_route import user_router
from app.database import verify_connection

app = FastAPI()
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if verify_connection():
    print("Database connection successful 🚀")
    app.include_router(user_router)
else:
    print("Database connection failed ❌")
    raise HTTPException(status_code=500, detail="Database connection failed ❌")
