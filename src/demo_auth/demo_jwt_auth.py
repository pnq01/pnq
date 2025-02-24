from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.security import (
    OAuth2PasswordBearer,
    HTTPBearer,
)
from src.api.schemas.schemas import UserSchemaTest
from src.auth import utils as auth_utils
from pydantic import BaseModel
from jwt import InvalidTokenError

from src.demo_auth.helpers import (
    ACCESS_TOKEN_TYPE,
    TOKEN_TYPE_FIELD,
    create_access_token,
    create_refresh_token,
)

http_bearer = HTTPBearer(auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/jwt/login")


class TokenInfo(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"


router = APIRouter(prefix="/jwt", tags=["JWT"], dependencies=[Depends(http_bearer)])

john = UserSchemaTest(
    username="john",
    password=auth_utils.hash_password("qwerty"),
    email="danpavkzm@mail.ru",
)

sam = UserSchemaTest(
    username="sam",
    password=auth_utils.hash_password("secret"),
)
users_db: dict[str, UserSchemaTest] = {
    john.username: john,
    sam.username: sam,
}


def validate_auth_user(
    username: str = Form(),
    password: str = Form(),
):
    unauth_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invali username or password",
    )
    if not (user := users_db.get(username)):
        raise unauth_exc

    if not auth_utils.validate_password(
        password=password,
        hashed_password=user.password,
    ):
        raise unauth_exc

    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user inactive",
        )

    return user


def get_current_token_payload(  # функция для получения payload токена
    # credentials: HTTPAuthorizationCredentials = Depends(
    #     http_bearer
    # ),  # Мы берем payload токена из заголовков запроса вот от сюда "credentials"
    token: str = Depends(
        oauth2_scheme
    ),  # здесь токен у нас сам автоматически по-новому обновляется
) -> UserSchemaTest:
    # token = credentials.credentials
    try:
        payload = auth_utils.decode_jwt(
            token=token,
        )  # этот payload мы декодим используя public key для проверки что он валидный и после этого возвращаем его
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"token invalid: {e}",
        )
    return payload


def get_current_auth_user(
    payload: dict = Depends(get_current_token_payload),
) -> UserSchemaTest:  # Получаем юзера находя
    token_type = payload.get(TOKEN_TYPE_FIELD)
    if token_type != ACCESS_TOKEN_TYPE:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"token invalid type {token_type!r} expected {ACCESS_TOKEN_TYPE!r}",
        )

    username: str | None = payload.get(
        "username"
    )  # Его username в токене и берем от туда sub(то есть о ком вообще речь.
    # Там обычно ранится либо id, либо username у меня)
    if user := users_db.get(username):  # Если есть, вытаскиваем юзера из базы данных
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid(user not found)",
    )


def get_current_active_auth_user(
    user: UserSchemaTest = Depends(get_current_auth_user),
):
    if user.active:
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="user inactive",
    )


@router.post("/login/", response_model=TokenInfo)
def auth_user_issue_jwt(
    user: UserSchemaTest = Depends(validate_auth_user),
):
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.get("/users/me/")  # Проверка информации о текущем пользователе
def auth_user_check_self_info(
    payload: dict = Depends(get_current_token_payload),
    user: UserSchemaTest = Depends(
        get_current_active_auth_user
    ),  # проверка, что такой-то пользователь
):
    iat = payload.get("iat")
    return {
        "username": user.username,
        "email": user.email,
        "logged_in_at": iat,
    }
