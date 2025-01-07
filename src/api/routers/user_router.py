from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.schemas import UserCreateSchema, UserSchema
from src.db.models import User
from src.db.database import get_async_session

router = APIRouter(prefix="/user", tags=["Пользователи"])


@router.post("/")
async def create_user(
    user: Annotated[UserCreateSchema, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    user_dict = user.model_dump()

    user_model = User(**user_dict)
    session.add(user_model)
    await session.commit()

    return {"success": True}


@router.get("/", response_model=list[UserSchema])
async def get_all_users(session: AsyncSession = Depends(get_async_session)):
    users = await session.execute(select(User))
    return users.scalars().all()


@router.get("/{user_id}", response_model=UserSchema)
async def get_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    user_id = await session.get(User, user_id)

    if not user_id:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    return user_id
