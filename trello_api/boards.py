from typing import Dict

# from urllib.parse import urljoin

from helpers.api_call import get_api_helper
from constant import (
    GET_ALL_BOARDS,
    BASE_URL,
    AUTH_PARAMS,
    BOARDS,
    LISTS,
    CARDS,
    ACTIONS,
)
from helpers.types import JSONObject


def get_all_boards(**params: Dict[str, str]) -> JSONObject:
    """
    Fetch all boards form trello

    Args:
        params: options for the boards

    Return:
        dict which contains board details

    """

    return get_api_helper(
        url=BASE_URL + GET_ALL_BOARDS,
        **params,
        **AUTH_PARAMS,
    )


def get_all_list_on_board(board_id: str, **params: Dict[str, str]) -> JSONObject:
    """
    Fetch all the list form boards

    Args:
        board_id: id of board from which list needs to be fetched
        params: options for the labels

    Return:
        dict which contains list details

    """

    return get_api_helper(
        f"{BASE_URL}{BOARDS}/{board_id}{LISTS}", **params, **AUTH_PARAMS
    )


def get_all_cards_on_the_board(board_id: str, **params: Dict[str, str]) -> JSONObject:
    """
    Fetch all the cards form boards

    Args:
        board_id: id of board from which cards needs to be fetched
        params: options for the labels

    Return:
        dict which contains cards details

    """
    return get_api_helper(
        f"{BASE_URL}{BOARDS}/{board_id}{CARDS}",
        **params,
        **AUTH_PARAMS,
    )
