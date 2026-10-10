from sqlalchemy import (
    ForeignKey,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from backend.models import TargetRole
from backend.models.base import BaseWithUUID
from backend.models.mixins import CreatedAtMixin


class Digest(BaseWithUUID, CreatedAtMixin):
    title: Mapped[str] = mapped_column(Text)
    target_role_id: Mapped[int] = mapped_column(
        ForeignKey("targetroles.id", ondelete="SET NULL"),
    )

    target_role: Mapped[TargetRole] = relationship(
        "TargetRole",
    )
