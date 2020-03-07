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


@add(api_base + 'friends/')
@leftadd('.json')
class Friends:
    ids = 'ids'
    list = 'list'


@add(api_base + 'statuses/')
@leftadd('.json')
class Statuses:
    update = 'update'
