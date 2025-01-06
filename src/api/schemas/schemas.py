from pydantic import BaseModel
from src.db.models import CheckAuthor, IsPublished, User


# Пользователи
class UserBaseSchema(BaseModel):
    login: str

    class Config:
        from_attributes = True


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int
    is_author: CheckAuthor


# Посты
class ArticleBaseSchema(BaseModel):
    title: str
    content: str

    class Config:
        from_attributes = True


class ArticleCreateSchema(ArticleBaseSchema):
    author_id: User
    # category_id: int
    # tags: list[int]


class ArticleSchema(ArticleBaseSchema):
    id: int
    is_published: IsPublished


# Категории
class CategoryBaseSchema(BaseModel):
    ...

    class Config:
        from_attributes = True


class CategoryCreateSchema(CategoryBaseSchema): ...


class CategorySchema(CategoryBaseSchema): ...


# Теги
class TagBaseSchema(BaseModel):
    ...

    class Config:
        from_attributes = True


class TagCreateSchema(TagBaseSchema): ...


class TagSchema(TagBaseSchema): ...
