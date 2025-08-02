from typing import TYPE_CHECKING

from geoalchemy2 import Geometry, WKTElement
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models import Base


__all__ = ["Building"]

if TYPE_CHECKING:
    from database.models import Organization


class Building(Base):
    """Модель Здания."""

    __tablename__ = "buildings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    address: Mapped[str] = mapped_column(nullable=False, unique=True)
    coordinates: Mapped[WKTElement] = mapped_column(Geometry(geometry_type="POINT", srid=4326), nullable=False)

    organizations: Mapped[list["Organization"]] = relationship(back_populates="building")
