from passlib.hash import bcrypt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def hash_pass(password: str) -> str:
    return pwd_context.hash(password)


async def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)
