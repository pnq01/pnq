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

    return {"success": True, "tag": tag}


@router.get("/", response_model=list[TagBaseSchema])
async def get_all_tags(session: AsyncSession = Depends(get_async_session)):
    tags = await session.execute(select(Tag))
    return tags.scalars().all()


@router.get("/{tag_id}", response_model=TagSchema)
async def get_tag(tag_id: int, session: AsyncSession = Depends(get_async_session)):
    tag = await session.get(Tag, tag_id)

    if not tag:
        raise HTTPException(status_code=404, detail="Тег не найден")
    return tag


@router.post("/{tag_id}")
async def update_tag_name(
    tag_id: int, new_name: str, session: AsyncSession = Depends(get_async_session)
):
    tag = await session.get(Tag, tag_id)

    if tag == None:
        raise HTTPException(status_code=404, detail="Тег не найден")
    tag.tag = new_name
    await session.commit()
    return {"new_tag_set": True, "tag": tag}


@router.delete("/{tag_id}")
async def delete_tag(tag_id: int, session: AsyncSession = Depends(get_async_session)):
    tag = await session.get(Tag, tag_id)

    if tag == None:
        raise HTTPException(status_code=404, detail="Тег не найден")
    await session.delete(tag)
    await session.commit()
    return {"succes_delete": True}
