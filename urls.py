# auto gen
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



@add(api_base + 'account/')
@leftadd('.json')
class Account:
    settings = 'settings'  # GET
    verify_credentials = 'verify_credentials'  # GET
    remove_profile_banner = 'remove_profile_banner'  # POST
    update_profile = 'update_profile'  # POST
    update_profile_banner = 'update_profile_banner'  # POST
    update_profile_image = 'update_profile_image'  # POST
@add(api_base + 'users/')
@leftadd('.json')
class Users:
    profile_banner = 'profile_banner'  # GET
    lookup = 'lookup'  # GET
    search = 'search'  # GET
    show = 'show'  # GET
    report_spam = 'report_spam'  # POST
@add(api_base + 'saved_searches/')
@leftadd('.json')
class Saved_Searches:
    list = 'list'  # GET
    create = 'create'  # POST
@add(api_base + 'followers/')
@leftadd('.json')
class Followers:
    ids = 'ids'  # GET
    list = 'list'  # GET
@add(api_base + 'friends/')
@leftadd('.json')
class Friends:
    ids = 'ids'  # GET
    list = 'list'  # GET
@add(api_base + 'friendships/')
@leftadd('.json')
class Friendships:
    incoming = 'incoming'  # GET
    lookup = 'lookup'  # GET
    no_retweets__ids = 'no_retweets/ids'  # GET
    outgoing = 'outgoing'  # GET
    show = 'show'  # GET
    create = 'create'  # POST
    destroy = 'destroy'  # POST
    update = 'update'  # POST
@add(api_base + 'lists/')
@leftadd('.json')
class Lists:
    list = 'list'  # GET
    members = 'members'  # GET
    members__show = 'members/show'  # GET
    memberships = 'memberships'  # GET
    ownerships = 'ownerships'  # GET
    show = 'show'  # GET
    statuses = 'statuses'  # GET
    subscribers = 'subscribers'  # GET
    subscribers__show = 'subscribers/show'  # GET
    subscriptions = 'subscriptions'  # GET
    create = 'create'  # POST
    destroy = 'destroy'  # POST
    members__create = 'members/create'  # POST
    members__create_all = 'members/create_all'  # POST
    members__destroy = 'members/destroy'  # POST
    members__destroy_all = 'members/destroy_all'  # POST
    subscribers__create = 'subscribers/create'  # POST
    subscribers__destroy = 'subscribers/destroy'  # POST
    update = 'update'  # POST
@add(api_base + 'blocks/')
@leftadd('.json')
class Blocks:
    ids = 'ids'  # GET
    list = 'list'  # GET
    create = 'create'  # POST
    destroy = 'destroy'  # POST
@add(api_base + 'mutes/')
@leftadd('.json')
class Mutes:
    users__ids = 'users/ids'  # GET
    users__list = 'users/list'  # GET
    users__create = 'users/create'  # POST
    users__destroy = 'users/destroy'  # POST
@add(api_base + 'statuses/')
@leftadd('.json')
class Statuses:
    update = 'update'  # POST

