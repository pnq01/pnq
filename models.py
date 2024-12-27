from datetime import datetime
from sqlalchemy import (
    ForeignKey,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

from database import Base


class CheckAuthor(enum.Enum):
    author = "yes"
    not_author = "no"


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    is_author: Mapped[CheckAuthor] = mapped_column(default=CheckAuthor.not_author)

    articles: Mapped[list["Article"]] = relationship(
        back_populates="user",
    )


class IsPublished(enum.Enum):
    published = "published"
    nonpublished = "nonpublished"


class Article(Base):
    __tablename__ = "article"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(index=True)
    content: Mapped[str] = mapped_column(nullable=False)
    is_published: Mapped[IsPublished] = mapped_column(default=IsPublished.nonpublished)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    # category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    # tags: Mapped[]
    date: Mapped[datetime] = mapped_column(default=func.now())

    # category: Mapped["Category"] = relationship(back_populates="articles")
    user: Mapped["User"] = relationship(
        back_populates="articles",
    )
    mark_tags: Mapped[list["Tag"]] = relationship(
        back_populates="articles",
        secondary="article_tag",
    )


# class Category(Base):
#     __tablename__ = "category"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(nullable=False, index=True)
#
#     articles: Mapped[list["Article"]] = relationship(back_populates="category")
#


class Tag(Base):
    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(primary_key=True)
    tag: Mapped[str] = mapped_column(nullable=False, index=True)

    articles: Mapped[list["Article"]] = relationship(
        back_populates="mark_tags",
        secondary="article_tag",
    )


class ArticleTag(Base):
    __tablename__ = "article_tag"

    article_id: Mapped[int] = mapped_column(ForeignKey("article.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"), primary_key=True)


# class UserArticle(Base):
#     __tablename__ = "user_articles"
#
#     author_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
#     article_id: Mapped[int] = mapped_column(ForeignKey("article.id"), primary_key=True)
