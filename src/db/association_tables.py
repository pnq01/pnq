from sqlalchemy import Table, Column, Integer, ForeignKey, UniqueConstraint

from src.db.database import Base

user_article_association_table = Table(
    "user_article_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("users.id"), nullable=False),
    Column("article_id", ForeignKey("articles.id"), nullable=False),
    UniqueConstraint("user_id", "article_id", name="idx_unique_user_article"),
)
