from fastapi import APIRouter, Depends
from typing import Annotated
from src.api.schemas.schemas import UserCreateSchema
from src.db.models import Category
from src.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/category", tags=["Категории"])


@router.post("")
async def create_category(
    category: Annotated[UserCreateSchema, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    category_dict = category.model_dump()

    category_model = Category(**category_dict)
    session.add(category_model)
    await session.commit()

    return {"success": True}
