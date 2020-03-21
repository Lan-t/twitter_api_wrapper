# auto gen
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


api.add_route('/account/settings', Account.Settings)
api.add_route('/account/verify_credentials', Account.Verify_Credentials)
api.add_route('/account/remove_profile_banner', Account.Remove_Profile_Banner)
api.add_route('/account/update_profile', Account.Update_Profile)
api.add_route('/account/update_profile_banner', Account.Update_Profile_Banner)
api.add_route('/account/update_profile_image', Account.Update_Profile_Image)
api.add_route('/users/profile_banner', Users.Profile_Banner)
api.add_route('/users/lookup', Users.Lookup)
api.add_route('/users/search', Users.Search)
api.add_route('/users/show', Users.Show)
api.add_route('/users/report_spam', Users.Report_Spam)
api.add_route('/saved_searches/list', Saved_Searches.List)
api.add_route('/saved_searches/create', Saved_Searches.Create)
api.add_route('/followers/ids', Followers.Ids)
api.add_route('/followers/list', Followers.List)
api.add_route('/friends/ids', Friends.Ids)
api.add_route('/friends/list', Friends.List)
api.add_route('/friendships/incoming', Friendships.Incoming)
api.add_route('/friendships/lookup', Friendships.Lookup)
api.add_route('/friendships/no_retweets/ids', Friendships.No_Retweets__Ids)
api.add_route('/friendships/outgoing', Friendships.Outgoing)
api.add_route('/friendships/show', Friendships.Show)
api.add_route('/friendships/create', Friendships.Create)
api.add_route('/friendships/destroy', Friendships.Destroy)
api.add_route('/friendships/update', Friendships.Update)
api.add_route('/lists/list', Lists.List)
api.add_route('/lists/members', Lists.Members)
api.add_route('/lists/members/show', Lists.Members__Show)
api.add_route('/lists/memberships', Lists.Memberships)
api.add_route('/lists/ownerships', Lists.Ownerships)
api.add_route('/lists/show', Lists.Show)
api.add_route('/lists/statuses', Lists.Statuses)
api.add_route('/lists/subscribers', Lists.Subscribers)
api.add_route('/lists/subscribers/show', Lists.Subscribers__Show)
api.add_route('/lists/subscriptions', Lists.Subscriptions)
api.add_route('/lists/create', Lists.Create)
api.add_route('/lists/destroy', Lists.Destroy)
api.add_route('/lists/members/create', Lists.Members__Create)
api.add_route('/lists/members/create_all', Lists.Members__Create_All)
api.add_route('/lists/members/destroy', Lists.Members__Destroy)
api.add_route('/lists/members/destroy_all', Lists.Members__Destroy_All)
api.add_route('/lists/subscribers/create', Lists.Subscribers__Create)
api.add_route('/lists/subscribers/destroy', Lists.Subscribers__Destroy)
api.add_route('/lists/update', Lists.Update)
api.add_route('/blocks/ids', Blocks.Ids)
api.add_route('/blocks/list', Blocks.List)
api.add_route('/blocks/create', Blocks.Create)
api.add_route('/blocks/destroy', Blocks.Destroy)
api.add_route('/mutes/users/ids', Mutes.Users__Ids)
api.add_route('/mutes/users/list', Mutes.Users__List)
api.add_route('/mutes/users/create', Mutes.Users__Create)
api.add_route('/mutes/users/destroy', Mutes.Users__Destroy)
api.add_route('/statuses/update', Statuses.Update)



if __name__ == '__main__':
    api.run(port=8080)

