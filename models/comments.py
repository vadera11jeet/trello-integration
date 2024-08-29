import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from models.cards import Card
from models.members import Member
from models.board import Board


class Comment(db.Model):
    id: so.Mapped[str] = so.mapped_column(sa.String(128), primary_key=True, index=True)

    commented_text: so.Mapped[str] = so.mapped_column(sa.String(1024), nullable=False)
    card: so.Mapped[Card] = so.relationship(back_populates="comment")

    card_id: so.Mapped[str] = so.mapped_column(
        sa.String(128),
        sa.ForeignKey("card.id"),
        index=True,
        name="fk_comment_association_card_id",
    )

    member: so.Mapped[Member] = so.relationship(back_populates="comment")

    member_id: so.Mapped[str] = so.mapped_column(
        sa.String(128),
        sa.ForeignKey("member.id"),
        index=True,
        name="fk_comment_association_member_id",
    )

    board: so.Mapped[Board] = so.relationship(back_populates="comment")
    board_id: so.Mapped[str] = so.mapped_column(
        sa.String(128),
        sa.ForeignKey("board.id"),
        index=True,
        name="fk_comment_association_board_id",
    )

    def __repr__(self) -> str:
        return "Comment <{}>".format(self.id)
