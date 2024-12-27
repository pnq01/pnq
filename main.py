from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Response
from fastapi.responses import FileResponse
import uvicorn
from authx import AuthX, AuthXConfig

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = FastAPI()

config = AuthXConfig()

config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_access_cookie"
config.JWT_TOKEN_LOCATION = ["cookies"]
security = AuthX(config=config)


# SessionDep = Annotated[AsyncSession, Depends(get_session)]


if __name__ == "__main__":
    uvicorn.run("main:app")
