from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials


security = HTTPBasic()


async def read_current_user(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return {"username": credentials.username, "password": credentials.password}
