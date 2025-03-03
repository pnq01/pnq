from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from src.core.config import settings


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


DATABASE_URL = "sqlite+aiosqlite:///./test.db"  # ДЛЯ SQLITE ТЕСТОВ позже поменять


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Асинхронная функция для удаления таблиц
async def drop_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# async_engine = create_async_engine(url=settings.DATABASE_URL_asyncpg, echo=True)
# async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)
async_engine = create_async_engine(url=DATABASE_URL, echo=True)
async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)


# Потом удалить
# Асинхронная функция для создания таблиц
async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Асинхронная функция для удаления таблиц
async def drop_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def get_async_session():
    async with async_session_factory() as session:
        yield session
