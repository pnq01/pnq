from datetime import datetime

from sqlalchemy import (
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

from .database import Base


class CheckAuthor(str, enum.Enum):
    author = "yes"
    not_author = "no"


class User(Base):
    # __table_args__ = {"extend_existing": True}  # можно удалить при алембике вроде

    login: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_author: Mapped[CheckAuthor] = mapped_column(default=CheckAuthor.not_author)

    articles: Mapped[list["Article"]] = relationship(
        secondary="user_article_association",
        back_populates="users",
    )


class IsPublished(enum.Enum):
    published = "published"
    nonpublished = "nonpublished"


class Tag(Base):
    tag: Mapped[str] = mapped_column(nullable=False, index=True)


class Category(Base):
    name: Mapped[str] = mapped_column(nullable=False, index=True)


class Article(Base):
    # __table_args__ = {"extend_existing": True}  # можно удалить при алембике вроде

    title: Mapped[str] = mapped_column(index=True, nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    is_published: Mapped[IsPublished] = mapped_column(default=IsPublished.nonpublished)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now()
    )

    users: Mapped[list["User"]] = relationship(
        secondary="user_article_association",
        back_populates="articles",
    )
    # category_id: Mapped[int]
    # tag_id: Mapped[int]
