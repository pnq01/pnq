from fastapi import APIRouter, Depends
from typing import Annotated
from src.api.schemas.schemas import TagCreateSchema
from src.db.models import Tag
from src.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/tag", tags=["Тэги"])


@router.post("")
async def create_tag(
    tag: Annotated[TagCreateSchema, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    tag_dict = tag.model_dump()

    tag_model = Tag(**tag_dict)
    session.add(tag_model)
    await session.commit()

    return {"success": True}
