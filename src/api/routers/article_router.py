from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from sqlalchemy import select
from src.db.models import Article
from src.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.schemas import (
    ArticleBaseSchema,
    ArticleCreateSchema,
    ArticleSchema,
)

router = APIRouter(prefix="/article", tags=["Посты"])


@router.post("")
async def create_article(
    article: Annotated[ArticleCreateSchema, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    article_dict = article.model_dump()

    article_model = Article(**article_dict)
    session.add(article_model)
    await session.commit()

    return {"success": True, "article": article}


@router.get("/", response_model=list[ArticleSchema])
async def get_all_articles(session: AsyncSession = Depends(get_async_session)):
    articles = await session.execute(select(Article))
    return articles.scalars().all()


@router.get("/{article_id}", response_model=ArticleSchema)
async def get_article(
    article_id: int, session: AsyncSession = Depends(get_async_session)
):
    article = await session.get(Article, article_id)

    if not article:
        raise HTTPException(status_code=404, detail="Тег не найден")
    return article


@router.post("/{article_id}")
async def update_article_name(
    article_id: int, new_name: str, session: AsyncSession = Depends(get_async_session)
):
    article = await session.get(Article, article_id)

    if article == None:
        raise HTTPException(status_code=404, detail="Пост не найден")
    article.name = new_name
    await session.commit()
    return {"new_article_set": True, "article": article}


@router.delete("/{article_id}")
async def delete_article(
    article_id: int, session: AsyncSession = Depends(get_async_session)
):
    article = await session.get(Article, article_id)

    if article == None:
        raise HTTPException(status_code=404, detail="Пост не найден")
    await session.delete(article)
    await session.commit()
    return {"succes_delete": True}
