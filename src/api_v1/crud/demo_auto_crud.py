import asyncio
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.db.database import get_async_session, async_session_factory
from src.db.models import User, Article


async def create_user(
    login: str,
    password: str,
    session: AsyncSession,
) -> User:
    user = User(
        login=login,
        hashed_password=password,
    )

    session.add(user)
    await session.commit()
    return user


async def create_article(
    title: str,
    content: str,
    session: AsyncSession,
) -> Article:
    article = Article(
        title=title,
        content=content,
    )

    session.add(article)
    await session.commit()
    return article


async def main_relations(
    session: AsyncSession,
):
    user_1 = await create_user("john", "qwerty", session)
    user_2 = await create_user("sam", "secret", session)
    article_1 = await create_article("Автодороги", "road road road road", session)
    article_2 = await create_article("Мосты", "Мосты Мосты Мосты Мосты", session)

    user_1 = await session.scalar(
        select(User)
        .where(User.id == user_1.id)
        .options(
            selectinload(User.articles),
        ),
    )
    user_2 = await session.scalar(
        select(User)
        .where(User.id == user_2.id)
        .options(
            selectinload(User.articles),
        ),
    )
    user_1.articles.append(article_1)
    user_2.articles.append(article_1)
    user_2.articles.append(article_2)

    await session.commit()


async def get_users_with_articles(session: AsyncSession) -> list[User]:
    stmt = (
        select(User)
        .options(
            selectinload(User.articles),
        )
        .order_by(User.id)
    )
    orders = await session.scalars(stmt)
    return list(orders)


async def demo_m2m(
    session: AsyncSession,
):
    # await main_relations(session)
    users = await get_users_with_articles(session)
    for user in users:
        print(user.login, user.hashed_password, "articles:")
        for article in user.articles:
            print("-", article.title, article.content, article.created_at)
