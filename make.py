sample_input = '''
GET account/settings
GET account/verify_credentials
GET users/profile_banner
POST account/remove_profile_banner
#POST account/settings
POST account/update_profile
#POST account/update_profile_background_image (retired)
POST account/update_profile_banner
POST account/update_profile_image
GET saved_searches/list
#GET saved_searches/show/:id
POST saved_searches/create
#POST saved_searches/destroy/:id

GET followers/ids
GET followers/list
GET friends/ids
GET friends/list
GET friendships/incoming
GET friendships/lookup
GET friendships/no_retweets/ids
GET friendships/outgoing
GET friendships/show
GET users/lookup
GET users/search
GET users/show
#GET users/suggestions (deprecated)
#GET users/suggestions/:slug (deprecated)
#GET users/suggestions/:slug/members (deprecated)
POST friendships/create
POST friendships/destroy
POST friendships/update

GET lists/list
GET lists/members
GET lists/members/show
GET lists/memberships
GET lists/ownerships
GET lists/show
GET lists/statuses
GET lists/subscribers
GET lists/subscribers/show
GET lists/subscriptions
POST lists/create
POST lists/destroy
POST lists/members/create
POST lists/members/create_all
POST lists/members/destroy
POST lists/members/destroy_all
POST lists/subscribers/create
POST lists/subscribers/destroy
POST lists/update

GET blocks/ids
GET blocks/list
GET mutes/users/ids
GET mutes/users/list
POST blocks/create
POST blocks/destroy
POST mutes/users/create
POST mutes/users/destroy
POST users/report_spam

POST statuses/update
'''


urls_prepend = '''# auto gen
base = 'https://api.twitter.com/'
auth_base = base + 'oauth/'
api_base = base + '1.1/'


def add(s):
    def decorator(cls):
        for attr_name in [i for i in dir(cls) if i[0] != '_']:
            if isinstance((attr := getattr(cls, attr_name, None)), str):
                setattr(cls, attr_name, s + attr)
        return cls

    return decorator


def leftadd(s):
    def decorator(cls):
        for attr_name in [i for i in dir(cls) if i[0] != '_']:
            if isinstance((attr := getattr(cls, attr_name, None)), str):
                setattr(cls, attr_name, attr + s)
        return cls

    return decorator


'''

views_prepend = '''# auto gen
from responder import Request, Response
from requests_oauthlib import OAuth1Session

from api_keys import API_KEY, API_SECRET_KEY
from urls import *


class Auth:
    def on_request(self, req: Request, res: Response):
        try:
            req.session['oauth_token']
            req.session['oauth_token_secret']
            req.session['user_id']
            req.session['screen_name']
        except KeyError:
            res.status_code = 401

    def session(self, req: Request) -> OAuth1Session:
        return OAuth1Session(API_KEY, API_SECRET_KEY, req.session['oauth_token'], req.session['oauth_token_secret'])


class Get(Auth):
    url: str = ''

    def on_get(self, req: Request, res: Response):
        if res.status_code == 401:
            return
        session = self.session(req)
        url = self.url + '?' + (req.url.params or '')
        response = session.get(url)
        res.media = response.json()
        res.status_code = response.status_code


class Post(Auth):
    url: str = ''

    async def on_post(self, req: Request, res: Response):
        if res.status_code == 401:
            return
        session = self.session(req)
        url = self.url + '?' + (req.url.params or '')
        response = session.post(url, data=await req.media())
        res.media = response.json()
        res.status_code = response.status_code


'''

main_prepend = '''# auto gen
from responder import API, Request, Response
from requests_oauthlib import OAuth1Session

from auth import authenticate, oauth_callback
from api_keys import DEBUG
from views import *


if DEBUG:
    api = API(cors=True, cors_params={
        'allow_origins': ['http://localhost', 'http://localhost:8000'],
        'allow_methods': ['GET', 'POST'],
        'allow_headers': ['*'],
    })
else:
    api = API()

api.add_route('/authenticate', authenticate)
api.add_route('/oauth_callback/', oauth_callback)

'''

main_append = '''

if __name__ == '__main__':
    api.run(port=8080)
'''


from collections import defaultdict
import sys


s = sample_input
d = defaultdict(list)
for i in s.strip().splitlines(False):
    if not i or i[0] == '#': continue
    m, full_path = i.split(' ', 1)
    class_name, path = full_path.split('/', 1)
    d[class_name].append((path, m))


sys.stdout = open('urls.py', 'w')
print(urls_prepend)

for k, p in d.items():
    print(f"@add(api_base + '{k}/')")
    print(f"@leftadd('.json')")
    print(f"class {k.title()}:")
    for i, m in p:
        print(f"    {i.replace('/', '__')} = '{i}'  # {m}")

print()


sys.stdout = open('views.py', 'w')

print(views_prepend)

for k, p in d.items():
    print(f"class {k.title()}:")
    for i, m in p:
        print(f"    class {i.replace('/', '__').title()}({m.title()}):")
        print(f"        url = {k.title()}.{i.replace('/', '__')}")

print()


sys.stdout = open('main.py', 'w')

print(main_prepend)

for k, p in d.items():
    for i, m in p:
        print(f"api.add_route('/{k}/{i}', {k.title()}.{i.replace('/', '__').title()})")

print()
print(main_append)
