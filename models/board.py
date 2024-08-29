import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Board(db.Model):
    # __tablename__ = "board"
    id: so.Mapped[str] = so.mapped_column(sa.String(128), primary_key=True, index=True)
    board_name: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=False)
    list: so.WriteOnlyMapped["List"] = so.relationship(
        back_populates="board", cascade="all, delete-orphan"
    )

    card: so.WriteOnlyMapped["Card"] = so.relationship(
        back_populates="board", cascade="all, delete-orphan"
    )

    comment: so.WriteOnlyMapped["Comment"] = so.relationship(
        back_populates="board", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return "<Board {}>".format(self.board_name)
