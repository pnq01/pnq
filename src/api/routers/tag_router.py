from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.schemas import TagBaseSchema, TagCreateSchema, TagSchema
from src.db.models import Tag
from src.db.database import get_async_session

router = APIRouter(prefix="/tag", tags=["Тэги"])


@router.post("/")
async def create_tag(
    tag: Annotated[TagCreateSchema, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    tag_dict = tag.model_dump()

    tag_model = Tag(**tag_dict)
    session.add(tag_model)
    await session.commit()

    return {"success": True}


@router.get("/", response_model=list[TagBaseSchema])
async def get_all_tags(session: AsyncSession = Depends(get_async_session)):
    tags = await session.execute(select(Tag))
    return tags.scalars().all()


@router.get("/{tag_id}", response_model=TagSchema)
async def get_tag(tag_id: int, session: AsyncSession = Depends(get_async_session)):
    tag_id = await session.get(Tag, tag_id)

    if not tag_id:
        raise HTTPException(status_code=404, detail="Тег не найден")
    return tag_id
