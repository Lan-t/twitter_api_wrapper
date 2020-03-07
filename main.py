from responder import API, Request, Response
from requests_oauthlib import OAuth1Session

from auth import authenticate, oauth_callback
from users import friends
from tweets import statuses


api = API()

api.add_route('/authenticate', authenticate)
api.add_route('/oauth_callback/', oauth_callback)

api.add_route('/friends/ids', friends.Ids)
api.add_route('/friends/list', friends.List)

api.add_route('/statuses/update', statuses.Update)


if __name__ == '__main__':
    api.run(port=8080)
