import bcrypt

# from fastapi.security import OAuth2PasswordBearer


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def hash_pass(password: str) -> str:  # Хэширование пароля
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=password.encode("utf-8"), salt=salt)
    return hashed_password.decode("utf-8")


async def check_pass(
    password: str, hashed_password: str
) -> bool:  # Проверка хэшированного пароля
    try:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
    except ValueError:
        return False
