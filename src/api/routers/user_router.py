from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.schemas import UserCreateSchema, UserSchema
from src.db.models import User
from src.db.database import get_async_session


router = APIRouter(prefix="/user", tags=["Пользователи"])


@router.post("")
async def create_user(
    user: Annotated[UserCreateSchema, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    user_dict = user.model_dump()

    user_model = User(**user_dict)
    session.add(user_model)
    await session.commit()

    return {"success": True, "user": user}


@router.get("", response_model=list[UserSchema])
async def get_all_users(session: AsyncSession = Depends(get_async_session)):
    users = await session.execute(select(User))
    return users.scalars().all()


@router.get("/{user_id}", response_model=UserSchema)
async def get_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    user = await session.get(User, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


@router.post("/{user_id}")
async def update_user_password(
    user_id: int, new_pass: str, session: AsyncSession = Depends(get_async_session)
):
    user = await session.get(User, user_id)

    if user == None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    user.password = new_pass
    await session.commit()
    return {"new_password_set": True, "user": user}


@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    # token: Annotated[str, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_async_session),
):
    user = await session.get(User, user_id)

    if user == None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    await session.delete(user)
    await session.commit()
    return {"succes_delete": True}


###TOKEN####
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/token")
async def get_token(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


def fake_decode_token(token):
    return UserCreateSchema(
        login=token + "fakedecoded", hashed_password=token + "fakedecoded"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@router.get("/users/me")
async def read_users_me(
    current_user: Annotated[UserCreateSchema, Depends(get_current_user)]
):
    return current_user
