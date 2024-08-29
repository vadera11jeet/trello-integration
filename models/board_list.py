import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from models.board import Board


class List(db.Model):
    id: so.Mapped[str] = so.mapped_column(sa.String(128), primary_key=True, index=True)
    label_name: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=False)
    board: so.Mapped[Board] = so.relationship(back_populates="list")
    board_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey(Board.id), index=True)

    def __repr__(self) -> str:
        return f"<List {self.label_name}>"
