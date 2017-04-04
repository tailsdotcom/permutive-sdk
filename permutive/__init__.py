# -*- coding: utf-8 -*-
from .base import RequestsHTTPClient
from .event import EventResource
from .user import UserResource

__author__ = """Dinesh Vitharanage"""
__email__ = 'dvitharanage@gmail.com'
__version__ = '0.2.0'


class Permutive(object):

    def __init__(self, private_api_key, request_timeout_seconds=5):
        if not private_api_key:
            raise RuntimeError(
                'Access key required for Permutive API but none given'
            )

        self.client = RequestsHTTPClient(private_api_key, request_timeout_seconds=request_timeout_seconds)
        self.events = EventResource(self.client)
        self.users = UserResource(self.client)

