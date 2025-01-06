from fastapi import APIRouter, Depends
from typing import Annotated
from src.api.schemas.schemas import ArticleCreateSchema
from src.db.models import Article
from src.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

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

    return {"success": True}
