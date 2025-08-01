from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models import Base


__all__ = ["Activity"]


class Activity(Base):
    """Модель Вида деятельности с древовидной структурой."""

    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    # TODO: Добавить индекс? Идет рекурсивный поиск по глубине в репозитории
    parent_id: Mapped[int | None] = mapped_column(ForeignKey("activities.id"))

    parent: Mapped["Activity"] = relationship(back_populates="children", remote_side=[id])
    children: Mapped[list["Activity"]] = relationship(back_populates="parent")
