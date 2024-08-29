import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class CardMemberAssociation(db.Model):
    card_id: so.Mapped[str] = so.mapped_column(
        sa.String(128),
        sa.ForeignKey("card.id"),
        nullable=False,
        primary_key=True,
        name="fk_card_member_association_card_id",
    )
    member_id: so.Mapped[str] = so.mapped_column(
        sa.String(128),
        sa.ForeignKey("member.id"),
        nullable=False,
        primary_key=True,
        name="fk_card_member_association_member_id",
    )

    card = so.relationship("Card", back_populates="card_associations")
    member = so.relationship("Member", back_populates="card_associations")
