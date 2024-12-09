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

engine = create_async_engine("sqlite+aiosqlite:///books.db")

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with new_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]


class Base(DeclarativeBase):
    pass


class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]


@app.get("/", summary="начальная страница", tags=["Главная"])
def root():
    return FileResponse("index.html")


@app.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"success": True}


class BookAddSchema(BaseModel):
    title: str
    author: str


class BookSchema(BookAddSchema):
    id: int


@app.post("/books")
async def create_book(data: BookAddSchema, session: SessionDep):
    new_book = BookModel(title=data.title, author=data.author)
    session.add(new_book)
    await session.commit()
    return {"success": True}


@app.get("/books")
async def get_books(session: SessionDep):
    query = select(BookModel)
    result = await session.execute(query)
    return result.scalars().all()


class UserLoginSchema(BaseModel):
    username: str
    password: str


@app.post("/login", tags=["Авторизация"])
async def login(creds: UserLoginSchema, response: Response):
    if creds.username == "test" and creds.password == "test":
        token = security.create_access_token(uid="12345")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")


@app.get("/protected", dependencies=[Depends(security.access_token_required)], tags=["Авторизация"])
async def protected():
    return {"access_permission": True}


if __name__ == "__main__":
    uvicorn.run("main:app")
