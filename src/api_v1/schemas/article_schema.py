from pydantic import BaseModel

from src.db.models import IsPublished


class ArticleBaseSchema(BaseModel):
    title: str
    content: str
    tag_id: int
    category_id: int

    # category: CategoryBaseSchema = None
    # user: UserBaseSchema = None
    # tag: list[TagBaseSchema] = []

    class Config:
        from_attributes = True


class ArticleCreateSchema(ArticleBaseSchema):
    pass


class ArticleSchema(ArticleBaseSchema):
    id: int
    is_published: IsPublished
