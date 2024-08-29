import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Member(db.Model):

    id: so.Mapped[str] = so.mapped_column(sa.String(128), primary_key=True, index=True)
    full_name: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=False)

    # This defines the association table relationship
    card_associations = so.relationship(
        "CardMemberAssociation", back_populates="member", cascade="all, delete-orphan"
    )

    # Define many-to-many relationship with Card via association table
    cards = so.relationship(
        "Card", secondary="card_member_association", back_populates="members"
    )

    comment: so.WriteOnlyMapped["Comment"] = so.relationship(
        back_populates="member", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Member {self.full_name}>"
