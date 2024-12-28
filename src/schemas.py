from pydantic import BaseModel
from src.models import CheckAuthor


class UserGetSchema(BaseModel):
    login: str
    is_author: CheckAuthor

    class Config:
        from_attributes = True


class UserAddSchema(UserGetSchema):
    password: str


class UserSchema(UserAddSchema):
    id: int
