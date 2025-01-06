from fastapi import APIRouter, Depends
from typing import Annotated
from src.api.schemas.schemas import UserSchema, UserAddSchema, UserGetSchema
from src.repositories.repository import UserRepository

router = APIRouter(prefix="/user", tags=["Пользователи"])


@router.post("")
async def user_add(user: Annotated[UserAddSchema, Depends()]):
    task_id = await UserRepository.add_user(user)
    return {"task_id": task_id, "ok": True}


@router.get("")
async def get_users():
    await UserRepository.get_user()
    return {"ok": True}


# @router.get("/{user_id}")
# async def get_user(user_id):
#     ///
#     return {"user": user}
