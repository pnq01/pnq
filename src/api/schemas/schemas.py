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


# # Категории
# class CategoryBaseSchema(BaseModel):
#     ...
#
#     class Config:
#         from_attributes = True
#
#
# class CategoryCreateSchema(CategoryBaseSchema): ...
#
#
# class CategorySchema(CategoryBaseSchema): ...
#
#


# Теги
class TagBaseSchema(BaseModel):
    tag: str

    class Config:
        from_attributes = True


class TagCreateSchema(TagBaseSchema):
    pass


class TagSchema(TagBaseSchema):
    id: int


# Посты
# class ArticleBaseSchema(BaseModel):
#     title: str
#     content: str

#     class Config:
#         from_attributes = True


# class ArticleCreateSchema(ArticleBaseSchema):
#     author_id: "UserSchema"  # int или UserSchema
#     tags: list[TagBaseSchema]
#     # category_id: int


# class ArticleSchema(ArticleBaseSchema):
#     id: int
#     is_published: IsPublished
