# auto gen
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



class Account:
    class Settings(Get):
        url = Account.settings
    class Verify_Credentials(Get):
        url = Account.verify_credentials
    class Remove_Profile_Banner(Post):
        url = Account.remove_profile_banner
    class Update_Profile(Post):
        url = Account.update_profile
    class Update_Profile_Banner(Post):
        url = Account.update_profile_banner
    class Update_Profile_Image(Post):
        url = Account.update_profile_image
class Users:
    class Profile_Banner(Get):
        url = Users.profile_banner
    class Lookup(Get):
        url = Users.lookup
    class Search(Get):
        url = Users.search
    class Show(Get):
        url = Users.show
    class Report_Spam(Post):
        url = Users.report_spam
class Saved_Searches:
    class List(Get):
        url = Saved_Searches.list
    class Create(Post):
        url = Saved_Searches.create
class Followers:
    class Ids(Get):
        url = Followers.ids
    class List(Get):
        url = Followers.list
class Friends:
    class Ids(Get):
        url = Friends.ids
    class List(Get):
        url = Friends.list
class Friendships:
    class Incoming(Get):
        url = Friendships.incoming
    class Lookup(Get):
        url = Friendships.lookup
    class No_Retweets__Ids(Get):
        url = Friendships.no_retweets__ids
    class Outgoing(Get):
        url = Friendships.outgoing
    class Show(Get):
        url = Friendships.show
    class Create(Post):
        url = Friendships.create
    class Destroy(Post):
        url = Friendships.destroy
    class Update(Post):
        url = Friendships.update
class Lists:
    class List(Get):
        url = Lists.list
    class Members(Get):
        url = Lists.members
    class Members__Show(Get):
        url = Lists.members__show
    class Memberships(Get):
        url = Lists.memberships
    class Ownerships(Get):
        url = Lists.ownerships
    class Show(Get):
        url = Lists.show
    class Statuses(Get):
        url = Lists.statuses
    class Subscribers(Get):
        url = Lists.subscribers
    class Subscribers__Show(Get):
        url = Lists.subscribers__show
    class Subscriptions(Get):
        url = Lists.subscriptions
    class Create(Post):
        url = Lists.create
    class Destroy(Post):
        url = Lists.destroy
    class Members__Create(Post):
        url = Lists.members__create
    class Members__Create_All(Post):
        url = Lists.members__create_all
    class Members__Destroy(Post):
        url = Lists.members__destroy
    class Members__Destroy_All(Post):
        url = Lists.members__destroy_all
    class Subscribers__Create(Post):
        url = Lists.subscribers__create
    class Subscribers__Destroy(Post):
        url = Lists.subscribers__destroy
    class Update(Post):
        url = Lists.update
class Blocks:
    class Ids(Get):
        url = Blocks.ids
    class List(Get):
        url = Blocks.list
    class Create(Post):
        url = Blocks.create
    class Destroy(Post):
        url = Blocks.destroy
class Mutes:
    class Users__Ids(Get):
        url = Mutes.users__ids
    class Users__List(Get):
        url = Mutes.users__list
    class Users__Create(Post):
        url = Mutes.users__create
    class Users__Destroy(Post):
        url = Mutes.users__destroy
class Statuses:
    class Update(Post):
        url = Statuses.update

