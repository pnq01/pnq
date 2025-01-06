from fastapi import APIRouter, Depends
from typing import Annotated
from src.api.schemas.schemas import UserCreateSchema
from src.db.models import User
from src.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

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

    return {"success": True}


# @router.get("")
# async def get_users():
#     await UserRepository.get_user()
#     return {"ok": True}


# @router.get("/{user_id}")
# async def get_user(user_id):
#     ///
#     return {"user": user}
