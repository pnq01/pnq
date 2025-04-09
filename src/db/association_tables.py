from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.db.database import Base

# user_article_association_table = Table(  # старый вид объявления связей
#     "user_article_association",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("user_id", ForeignKey("users.id"), nullable=False),
#     Column("article_id", ForeignKey("articles.id"), nullable=False),
#     UniqueConstraint("user_id", "article_id", name="idx_unique_user_article"),
# )


class UserArticleAssociation(Base):  # новый вид объявления связей
    __tablename__ = "user_article_association"
    table_name = (
        UniqueConstraint(
            "user_id",
            "article_id",
            name="idx_unique_user_article",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"))
