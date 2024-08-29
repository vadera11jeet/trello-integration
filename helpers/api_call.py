import requests
from typing import Dict
from helpers.types import JSONObject


def get_api_helper(url: str, **params: Dict[str, str]) -> JSONObject:
    """
    Method helps to make get api call

    Args:
        url : where to make get api call
        **params : query parameters

    Returns:
        api response in json format

    """
    print(f"calling api {url} ...\n")
    response = requests.get(url, params)
    print(response.url)
    print()

    data = response.json()
    # print(data)
    return data
