from pydantic import BaseModel
from src.db.models import CheckAuthor, IsPublished, User


class UserBaseSchema(BaseModel):
    login: str
    is_author: CheckAuthor


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int

    class Config:
        from_attributes = True


class ArticleBaseSchema(BaseModel):
    title: str
    content: str
    is_published: IsPublished


class ArticleCreateSchema(ArticleBaseSchema):
    author_id: int


class ArticleSchema(ArticleBaseSchema):
    id: int

    class Config:
        from_attributes = True
