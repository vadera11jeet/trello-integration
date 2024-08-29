import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from models.board import Board


class Card(db.Model):

    id: so.Mapped[str] = so.mapped_column(sa.String(128), primary_key=True, index=True)
    card_name: so.Mapped[str] = so.mapped_column(sa.String(512), nullable=False)
    card_description: so.Mapped[str] = so.mapped_column(sa.String(1024), nullable=True)

    board_id: so.Mapped[str] = so.mapped_column(
        sa.String(128),
        sa.ForeignKey("board.id"),
        index=True,
        name="fk_card_association_board_id",
    )
    board = so.relationship("Board", back_populates="card")

    # Correct relationship with CardMemberAssociation
    card_associations = so.relationship(
        "CardMemberAssociation", back_populates="card", cascade="all, delete-orphan"
    )
    comment: so.WriteOnlyMapped["Comment"] = so.relationship(
        back_populates="card", cascade="all, delete-orphan"
    )

    # Many-to-Many with Member through association table
    members = so.relationship(
        "Member", secondary="card_member_association", back_populates="cards"
    )

    def __repr__(self) -> str:
        return f"<Card {self.card_name}>"
