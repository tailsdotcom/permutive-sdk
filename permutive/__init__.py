# -*- coding: utf-8 -*-
from .base import RequestsHTTPClient
from .event import Event
from .user import User

__author__ = """Dinesh Vitharanage"""
__email__ = 'dvitharanage@gmail.com'
__version__ = '0.1.0'


class Permutive(object):

    def __init__(self, private_api_key):
        if not private_api_key:
            raise RuntimeError(
                'Access key required for Permutive API but none given'
            )
        self.client = RequestsHTTPClient(private_api_key)
        self.events = Event(self.client)
        self.users = User(self.client)

