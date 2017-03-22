from permutive.base import RequestsHTTPClient
from permutive.event import Event
from permutive.user import User


class Permutive(object):

    def __init__(self, private_api_key):
        if not private_api_key:
            raise RuntimeError(
                'Access key required for Permutive API but none given'
            )
        self.client = RequestsHTTPClient(private_api_key)
        self.events = Event(self.client)
        self.users = User(self.client)

