from typing import List
from flask import Flask, Request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
from trello_api.boards import (
    get_all_boards,
    get_all_list_on_board,
    get_all_cards_on_the_board,
)
from trello_api.cards import get_all_members_of_the_card, get_comments_on_cards
from helpers.types import JSONObject

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
from models.board import Board
from models.board_list import List
from models.cards import Card
from models.members import Member
from models.comments import Comment
from models.cards_members import CardMemberAssociation

migrate = Migrate(app, db)


"""
    @app.shell_context_process decorator is used to provide variable & import context to flask shell
    @app.shell_context_processor
    def make_shell_context():
        return { "db":db, "so":so, "sa":sa }
"""


@app.get("/sync")
def sync_trello_db():
    board_list: List[JSONObject] = get_all_boards()
    board_ids: List[str] = list(map(lambda board: board.get("id", ""), board_list))
    boards = list(
        map(
            lambda board: Board(id=board.get("id"), board_name=board.get("name")),
            board_list,
        )
    )
    # print(boards)

    # print("hello")
    cards_on_boards = list(map(lambda id: get_all_cards_on_the_board(id), board_ids))

    print(len(cards_on_boards[0]))

    lists = list(
        map(
            lambda list_info: List(
                id=list_info.get("id"),
                label_name=list_info.get("name"),
                board_id=list_info.get("idBoard"),
            ),
            cards_on_boards[0],
        )
    )

    cards_on_boards = list(map(lambda id: get_all_cards_on_the_board(id), board_ids))
    card_ids: List[str] = list(map(lambda cards: cards.get("id"), cards_on_boards[0]))
    member_list = list(
        map(lambda card_id: get_all_members_of_the_card(card_id), card_ids)
    )
    members = list(
        map(
            lambda member: Member(
                id=member.get("id"), full_name=member.get("fullName")
            ),
            member_list[0],
        )
    )

    card_members_association = []
    cards = []
    for card in cards_on_boards[0]:
        cards.append(
            Card(
                id=card.get("id"),
                card_name=card.get("name"),
                card_description=card.get("description"),
                board_id=card.get("idBoard"),
            )
        )

        for member_id in card.get("idMembers"):
            card_members_association.append(
                CardMemberAssociation(card_id=card.get("id"), member_id=member_id)
            )

    comment_list = list(map(lambda card_id: get_comments_on_cards(card_id), card_ids))

    print(len(comment_list))
    comments = []

    for comment in comment_list:
        if len(comment) and comment[0].get("data").get("text"):
            # print("comment text ", comment.get("data"))
            comments.append(
                Comment(
                    id=comment[0].get("id"),
                    card_id=comment[0].get("data").get("card").get("id"),
                    board_id=comment[0].get("data").get("board").get("id"),
                    member_id=comment[0].get("idMemberCreator"),
                    commented_text=comment[0].get("data").get("text"),
                )
            )

    print(comments)

    try:
        db.session.bulk_save_objects(
            boards + lists + members + cards + card_members_association + comments
        )
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("exception ocurred")
        print(e)

    return jsonify({"status": "success"})


if __name__ == "__main__":

    board_list: List[JSONObject] = get_all_boards()
    print(len(board_list))

    board_ids: List[str] = list(map(lambda board: board.get("id", ""), board_list))

    # print("================= board ids =========================")
    # print(board_ids)
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    list_on_board: List[JSONObject] = list(
        map(lambda id: get_all_list_on_board(board_id=id), board_ids)
    )

    # print("================= list on boards =========================")
    # print(list_on_board)
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    cards_on_boards = list(map(lambda id: get_all_cards_on_the_board(id), board_ids))
    # print("============================ cards =========================")
    # print((cards_on_boards))
    # print("=============================================================")
    card_ids: List[str] = list(map(lambda cards: cards.get("id"), cards_on_boards[0]))
    # print(card_ids)

    members = list(map(lambda card_id: get_all_members_of_the_card(card_id), card_ids))

    # print("++++++++++++++++ members +++++++++++++++++++++++++")
    # print(members)
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    comments = list(map(lambda card_id: get_comments_on_cards(card_id), card_ids))

    print("++++++++++++++++ comments +++++++++++++++++++++++++")
    print(comments)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
