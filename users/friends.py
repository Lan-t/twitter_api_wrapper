from responder import Request, Response, API

from urls import Friends
from views import Get


class Ids(Get):
    url = Friends.ids


class List(Get):
    url = Friends.list
