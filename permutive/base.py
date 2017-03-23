# -*- coding: utf-8 -*-
import requests

from .exceptions import PermutiveApiException


class HTTPClient(object):
    BASE_URL = 'https://api.permutive.com/'

    def __init__(self, private_key, base_url=None, api_version='v1.1'):
        self._headers = {
            'X-API-Key': private_key
        }
        self.base_url = (base_url or self.BASE_URL).rstrip('/')
        self.api_version = api_version

    def request(self, method, endpoint, data=None, headers=None,):
        """
         Makes a request to the Permutive API and parses the response.
         Non 200 responses raises PermutiveApiException
        :param method: string HTTP method (upper or lowercase)
        :param endpoint: string resource endpoint. eg: /events
        :param data: (optional) dict request body to be json or url encoded, depending on HTTP method
        :param headers: (optional) dict 
        :return: dict if the response contains a body, boolean True for HTTP 204
        """
        raise NotImplementedError('HTTPClient subclasses must implement `request`')


class Resource(object):
    """
    Base interface for all Permutive Api resources. 
     A resource is an object with a type, associated data, relationships to other resources, 
     and a set of methods that operate on it. e.g: /events endpoint represents resources of Event type. 
     
     Each subclass of :class:`Resource` should map to a /resource in the API and provide interfaces for
     all the methods offered by the API. i.e. GET /events, POST /events etc.
    """
    def __init__(self, client, **kwargs):
        self.client = client
        self.__dict__.update(kwargs)


class RequestsHTTPClient(HTTPClient):
    """
    HTTP transport client that uses requests package
    see: https://github.com/kennethreitz/requests
    """

    def request(self, method, endpoint, data=None, headers=None):
        uri = "{base_url}/{api_version}/{endpoint}".format(
            base_url=self.base_url,
            api_version=self.api_version,
            endpoint=endpoint.strip('/')
        )
        try:
            self._headers.update(headers)
        except TypeError:
            pass

        if method == 'GET':
            response = requests.get(uri, headers=self._headers, params=data)
        else:
            response = requests.request(method.upper(), uri, headers=self._headers, json=data)

        if not response.ok:
            raise PermutiveApiException(response)
        try:
            return response.json()
        except ValueError:
            # Non error status with empty body
            return True

