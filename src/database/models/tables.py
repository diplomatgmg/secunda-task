from sqlalchemy import Column, ForeignKey, Table

from database.models import Base


__all__ = ["organization_activity_table"]

organization_activity_table = Table(
    "organization_activity_table",
    Base.metadata,
    Column("organization_id", ForeignKey("organizations.id"), primary_key=True),
    Column("activity_id", ForeignKey("activities.id"), primary_key=True),
)
