from fastapi import FastAPI, Depends
from typing import Annotated
from schemas import UserSchema, UserAddSchema, UserGetSchema
from models import CheckAuthor


app = FastAPI()

users = []


@app.post("/user")
async def user_add(user: Annotated[UserAddSchema, Depends()]):
    user = UserAddSchema(login="root", password="1234", is_author=CheckAuthor.author)
    users.append(user)
    return {"user_for_add": user, "ok": True}


@app.get("/user")
async def get_users():
    return {"user": users}


# @app.get("/user/{user_id}")
# async def get_user(user_id):
#     ///
#     return {"user": user}
