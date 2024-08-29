from typing import Dict
from helpers.api_call import get_api_helper
from constant import BASE_URL, AUTH_PARAMS, MEMBERS, CARDS, ACTIONS
from helpers.types import JSONObject


def get_all_members_of_the_card(card_id: str, **params: Dict[str, str]) -> JSONObject:
    """
    Fetch all members of card

    Args:
        card_id: card id for which members needs to be fetched
        params: options for the cards

    Return:
        list of dict which contains members details

    """

    return get_api_helper(
        f"{BASE_URL}{CARDS}/{card_id}{MEMBERS}", **AUTH_PARAMS, **params
    )


def get_comments_on_cards(card_id: str, **params: Dict[str, str]) -> JSONObject:
    """
    Fetch all comments of card

    Args:
        card_id: card id for which comments needs to be fetched
        params: options for the cards

    Return:
        list of dict which contains comments details

    """

    return get_api_helper(
        f"{BASE_URL}{CARDS}/{card_id}{ACTIONS}",
        **AUTH_PARAMS,
        **params,
    )
