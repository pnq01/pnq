from pydantic import BaseModel, EmailStr
from src.db.models import CheckAuthor, IsPublished, User


# Пользователи
class UserBaseSchema(BaseModel):
    login: str

    class Config:
        from_attributes = True


class UserCreateSchema(UserBaseSchema):
    hashed_password: str


class UserSchema(UserBaseSchema):
    id: int
    is_author: CheckAuthor


# ----
class UserSchemaTest(BaseModel):
    username: str
    password: bytes
    email: EmailStr | None = None
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
    tag: str

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
    author_id: int
    tag_id: int
    category_id: int

    # category: CategoryBaseSchema = None
    # user: UserBaseSchema = None
    # mark_tags: list[TagBaseSchema] = []

    class Config:
        from_attributes = True


class ArticleCreateSchema(ArticleBaseSchema):
    pass


class ArticleSchema(ArticleBaseSchema):
    id: int
    is_published: IsPublished
