from typing import Final
from urllib.parse import parse_qsl, quote, unquote, parse_qs
import json
from uuid import uuid4

from responder import API, Request, Response
from requests_oauthlib import OAuth1Session

from api_keys import API_KEY, API_SECRET_KEY

api_url_base: Final = ''

request_token_url: Final = 'https://api.twitter.com/oauth/request_token'
authenticate_url: Final = 'https://api.twitter.com/oauth/authenticate'
access_token_url: Final = 'https://api.twitter.com/oauth/access_token'
callback_url: Final = 'http://localhost:8080/oauth_callback/'
after_redirect_url: Final = '/app'


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


def authenticate(req: Request, res: Response):
    session = OAuth1Session(API_KEY, API_SECRET_KEY)
    response = session.post(request_token_url, params={
        'oauth_callback': callback_url
    })

    tokens = dict(parse_qsl(response.text))
    oauth_token = tokens['oauth_token']

    res.redirect(authenticate_url + f'?oauth_token={oauth_token}')


def oauth_callback(req: Request, res: Response, ):
    oauth_token = req.params['oauth_token']
    oauth_verifier = req.params['oauth_verifier']

    session = OAuth1Session(API_KEY, API_SECRET_KEY, oauth_token, oauth_verifier)
    response = session.post(access_token_url, params={
        'oauth_verifier': oauth_verifier
    })

    access_token = dict(parse_qsl(response.text))
    res.session['oauth_token'] = access_token['oauth_token']
    res.session['oauth_token_secret'] = access_token['oauth_token_secret']
    res.session['user_id'] = access_token['user_id']
    res.session['screen_name'] = access_token['screen_name']

    res.redirect(after_redirect_url)
