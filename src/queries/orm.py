from src.database import async_engine, get_session
from src.models import User
from src.database import Base


def create_table():
    Base.metadata.drop_all(async_engine)
    async_engine.echo = False
    Base.metadata.create_all(async_engine)
    async_engine.echo = True


async def insert_data():
    async with get_session() as session:
        user = User(login="danil", password="danil")
        session.add(user)
        await session.commit()
