from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from sqlalchemy import select
from src.api.schemas.schemas import CategoryCreateSchema, CategorySchema
from src.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession


from src.db.models import Category

router = APIRouter(prefix="/category", tags=["Категории"])


@router.post("")
async def create_category(
    category: Annotated[CategoryCreateSchema, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    category_dict = category.model_dump()

    category_model = Category(**category_dict)
    session.add(category_model)
    await session.commit()

    return {"success": True, "category": category}


@router.get("", response_model=list[CategorySchema])
async def get_all_categorys(session: AsyncSession = Depends(get_async_session)):
    categorys = await session.execute(select(Category))
    return categorys.scalars().all()


@router.get("/{category_id}", response_model=CategorySchema)
async def get_category(
    category_id: int, session: AsyncSession = Depends(get_async_session)
):
    category = await session.get(Category, category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    return category


@router.post("/{category_id}")
async def update_category_name(
    category_id: int, new_name: str, session: AsyncSession = Depends(get_async_session)
):
    category = await session.get(Category, category_id)

    if category == None:
        raise HTTPException(status_code=404, detail="Категория не найден")
    category.name = new_name
    await session.commit()
    return {"new_category_set": True, "category": category}


@router.delete("/{category_id}")
async def delete_category(
    category_id: int, session: AsyncSession = Depends(get_async_session)
):
    category = await session.get(Category, category_id)

    if category == None:
        raise HTTPException(status_code=404, detail="Тег не найден")
    await session.delete(category)
    await session.commit()
    return {"succes_delete": True}
