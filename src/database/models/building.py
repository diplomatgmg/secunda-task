from geoalchemy2 import Geometry, WKTElement
from sqlalchemy.orm import Mapped, mapped_column

from database.models import Base


__all__ = ["Building"]


class Building(Base):
    """Модель Здания."""

    __tablename__ = "buildings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    address: Mapped[str] = mapped_column(nullable=False, unique=True)
    coordinates: Mapped[WKTElement] = mapped_column(Geometry(geometry_type="POINT", srid=4326), nullable=False)
