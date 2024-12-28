from fastapi import FastAPI, Depends

from .router import router as user_router

# from typing import Annotated
# from src.schemas import UserSchema, UserAddSchema, UserGetSchema
# from src.models import CheckAuthor
# from src.repository import UserRepository


app = FastAPI()

app.include_router(user_router)
