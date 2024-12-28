from sqlalchemy import select
from .database import async_session_factory
from .schemas import UserAddSchema
from .models import User


class UserRepository:
    @classmethod
    async def add_user(cls, user: UserAddSchema):
        async with async_session_factory() as session:
            user_dict = user.model_dump()

            user_model = User(**user_dict)
            session.add(user_model)
            await session.flush()
            # После того как мы делаем флюш у нас запрос исполняется и все изменения сессии добавятся
            # в бд перед комитом уже и после этого у нас будет первичный ключ который мы выводим после коммита
            await session.commit()
            return user_model.id

    @classmethod
    async def get_user(cls):
        async with async_session_factory() as session:
            query = select(User)
            result = await session.execute(query)
            user_models = result.scalars().all()
            return user_models
