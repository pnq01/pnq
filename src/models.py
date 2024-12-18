from datetime import datetime
from sqlalchemy import  ForeignKey, MetaData, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

from src.database import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]
    is_author: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return f"User('id={self.id}', login={self.login}', password='{self.password}', is_author='{self.is_author}')"



class IsPublished(enum.Enum):
    published = "published"
    nonpublished = "nonpublished"


class Article(Base):
    __tablename__ = "article"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(index=True)
    content: Mapped[str] = mapped_column(nullable=False)
    is_published: Mapped[IsPublished]
    author: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE")) # Поменять что множество авторов будет!
    category: Mapped[str] # Mapped[Category] = mapped_column(ForeignKey("categories.id"))
    tags: Mapped[str] # Mapped[Tag] = mapped_column(ForeignKey("tags.id"))
    date: Mapped[datetime] = mapped_column(default=func.now())

    # user: Mapped[User] = relationship(back_populates="Статья")
    # category: Mapped[Category] = relationship(back_populates="Статья")
    # tag: Mapped[Tags] = relationship(back_populates="Статья")

    def __repr__(self):
        return (f"Article('id={self.id}', title={self.title}', content='{self.content}',"
                f" is_published={self.is_published}', author='{self.author}',"
                f" category={self.category}', tags='{self.tags}',date={self.date}')")


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, index=True)

    def __repr__(self):
        return f"Category('id={self.id}', 'name={self.name}')"


class Tag(Base):
    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(primary_key=True)
    tag: Mapped[str] = mapped_column(nullable=False, index=True)

    def __repr__(self):
        return f"Tag('id={self.id}', tag='{self.tag}')"
