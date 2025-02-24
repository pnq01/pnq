from src.api.schemas.schemas import UserSchemaTest
from src.auth import utils as auth_utils

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
