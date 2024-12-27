from pydantic import BaseModel
from models import CheckAuthor


class UserGetSchema(BaseModel):
    login: str
    is_author: CheckAuthor

    class Config:
        orm_mode = True


class UserAddSchema(UserGetSchema):
    password: str


class UserSchema(UserAddSchema):
    id: int
