from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.db.models import User, Article, Tag, Category


async def create_user(
    username: str,
    email: str,
    password: str,
    session: AsyncSession,
) -> User:
    user = User(
        username=username,
        email=email,
        password=password,
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


async def create_tag(
    name: str,
    session: AsyncSession,
) -> Tag:
    tag = Tag(
        name=name,
    )

    session.add(tag)
    await session.commit()
    return tag


async def create_category(
    name: str,
    session: AsyncSession,
) -> Category:
    category = Category(
        name=name,
    )

    session.add(category)
    await session.commit()
    return category


async def main_relations(
    session: AsyncSession,
):
    user_1 = await create_user("john", "danpavkznm@mail.ru", "qwerty", session)
    user_2 = await create_user("sam", "qaloto@mail.ru", "secret", session)

    category_1 = await create_category("Дороги", session)
    category_2 = await create_category("ПГС", session)

    article_1 = await create_article("Автодороги", "road road road road", session)
    article_2 = await create_article("Мосты", "Мосты Мосты Мосты Мосты", session)

    tag_1 = await create_tag("it в строительстве", session)
    tag_2 = await create_tag("Сопромат", session)

    user_1 = await session.scalar(
        select(User)
        .where(User.id == user_1.id)
        .options(
            selectinload(User.article),
        ),
    )
    user_2 = await session.scalar(
        select(User)
        .where(User.id == user_2.id)
        .options(
            selectinload(User.article),
        ),
    )

    article_1 = await session.scalar(
        select(Article)
        .where(Article.id == article_1.id)
        .options(
            selectinload(Article.tag),
            selectinload(Article.category),
        ),
    )
    article_2 = await session.scalar(
        select(Article)
        .where(Article.id == article_1.id)
        .options(
            selectinload(Article.tag),
            selectinload(Article.category),
        ),
    )

    article_1.tag.append(tag_1)
    article_1.tag.append(tag_2)
    article_2.tag.append(tag_1)

    article_1.category_id = category_1.id
    article_2.category_id = category_2.id

    user_1.article.append(article_1)
    user_2.article.append(article_1)
    user_2.article.append(article_2)

    await session.commit()


async def get_users_with_articles(session: AsyncSession) -> list[User]:
    stmt = (
        select(User)
        .options(
            selectinload(User.article),
            selectinload(Article.category),
            selectinload(Article.tag),
        )
        .order_by(User.id)
    )
    orders = await session.scalars(stmt)
    return list(orders)


async def demo_m2m(
    session: AsyncSession,
):
    await main_relations(session)
    users = await get_users_with_articles(session)
    for user in users:
        print(user.username, user.email, user.password, user.is_author, "articles:")
        for article in user.article:
            print("-", article.title, article.content, article.created_at)
