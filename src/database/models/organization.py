from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models import Base
from database.models.tables import organization_activity_table


__all__ = [
    "Organization",
    "PhoneNumber",
]

if TYPE_CHECKING:
    from database.models import Activity, Building


class PhoneNumber(Base):
    """Модель Номера телефона."""

    __tablename__ = "phone_numbers"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(nullable=False)

    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
    organization: Mapped["Organization"] = relationship(back_populates="phone_numbers")


class Organization(Base):
    """Модель Организации."""

    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)

    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"))
    building: Mapped["Building"] = relationship(back_populates="organizations")

    phone_numbers: Mapped[list["PhoneNumber"]] = relationship(back_populates="organization")

    activities: Mapped[list["Activity"]] = relationship(
        secondary=organization_activity_table, back_populates="organizations"
    )
