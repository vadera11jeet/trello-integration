import os

from dotenv import load_dotenv

load_dotenv()

# API endpoints
GET_ALL_BOARDS = "/members/me/boards"
BOARDS = "/boards"
LISTS = "/lists"
CARDS = "/cards"
ACTIONS = "/actions"
MEMBERS = "/members"


# base URL
BASE_URL = "https://api.trello.com/1"


AUTH_PARAMS = {
    "token": os.getenv("TRELLO_API_SECRET"),
    "key": os.getenv("TRELLO_API_KEY"),
}
