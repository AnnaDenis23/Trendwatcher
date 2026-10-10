import uuid

from sqlalchemy import (
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from backend.models.base import BaseWithUUID
from backend.models.publication_clusters import PublicationCluster
from backend.models.signals import Signal


class SignalSource(BaseWithUUID):
    signal_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("signals.id", ondelete="CASCADE"),
    )
    publication_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("rawpublications.id", ondelete="CASCADE"),
    )

    signal: Mapped[Signal] = relationship(
        "Signal",
    )
    publication: Mapped[PublicationCluster] = relationship(
        "RawPublication"
    )
