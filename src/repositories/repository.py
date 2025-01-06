from sqlalchemy import select
from ..db.database import async_session_factory, get_async_session
from ..api.schemas.schemas import UserAddSchema
from ..db.models import User
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


# class UserRepository:
#     @classmethod
#     async def add_user(
#         cls, user: UserAddSchema, session: AsyncSession = Depends(get_async_session)
#     ):
#         user_dict = user.model_dump()

#         user_model = User(**user_dict)
#         session.add(user_model)
#         await session.flush()
#         await session.commit()
#         return user_model.id

#     @classmethod
#     async def get_user(cls, session: AsyncSession = Depends(get_async_session)):
#         async with async_session_factory() as session:
#             query = select(User)
#             result = await session.execute(query)
#             user_models = result.scalars().all()
#             return user_models
