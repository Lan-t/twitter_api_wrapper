from responder import Request, Response
from requests_oauthlib import OAuth1Session

from api_keys import API_KEY, API_SECRET_KEY


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
