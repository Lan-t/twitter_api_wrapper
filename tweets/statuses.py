from views import Get, Post
from urls import Statuses


class Update(Post):
    url = Statuses.update
