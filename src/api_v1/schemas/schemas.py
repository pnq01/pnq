from pydantic import BaseModel, EmailStr
from src.db.models import CheckAuthor, IsPublished, User


# Пользователи
class UserBaseSchema(BaseModel):
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int
    is_author: CheckAuthor
    # articles добавить для вывода постов пользователя мб


# ----
class UserSchemaTest(BaseModel):
    username: str
    password: bytes
    email: EmailStr
    active: bool = True


# ----
# Категории
class CategoryBaseSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True


class CategoryCreateSchema(CategoryBaseSchema):
    pass


class CategorySchema(CategoryBaseSchema):
    id: int


# Теги
class TagBaseSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True


class TagCreateSchema(TagBaseSchema):
    pass


class TagSchema(TagBaseSchema):
    id: int


# Посты
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
