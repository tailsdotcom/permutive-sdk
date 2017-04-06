# -*- coding: utf-8 -*-
from permutive.exceptions import PermutiveApiException
from .util import none_default_namedtuple
from .base import Resource

User = none_default_namedtuple('User', 'id, custom_id, properties, updated')


class UserResource(Resource):

    def create(self):
        """
        Creates a new user in remote
        :return: User object consisting of only an id
        """
        result = self.client.request('POST', '/users')
        return User(**result)

    def identify(self, user_id, custom_id, **properties):
        """
        Associate a user to a known custom_id. This custom id can then be used to fetch a user using self.get
        :param user_id: string Permutive user_id (eg: from a object returned from self.create) 
        :param custom_id: string or stringifyable value. 
        :param properties: user properties
        :return: User
        """
        result = self.client.request('POST', '/identify', data={
            'id': user_id,
            'custom_id': str(custom_id),
            'properties': properties
        })
        return User(result.get('id'), custom_id, properties)

    def create_and_identify(self, custom_id, **properties):
        """
        Convenience method that calls self.create and self.identify sequentially 
        :param custom_id: string or stringifyable value. 
        :param properties: user properties
        :return: User
        """
        user = self.create()
        if not user.id:
            raise ValueError('Id was not present in the response from Permutive API')

        return self.identify(user.id, custom_id, **properties)

    def get(self, custom_id):
        """
        Fetch a user from remote using a custom id
        :param custom_id: string or stringifyable value. 
        :return: User|None
        """
        try:
            result = self.client.request('GET', '/identities/{}'.format(custom_id))
            result['id'] = result.pop('user_id')  # smh
            result['custom_id'] = custom_id
            return User(**result)
        except PermutiveApiException, e:
            if e.status_code == 404:
                return None
            else:
                raise e

    def update(self, custom_id, **properties):
        """
        Performs a partial update of a User object on remote. 
        NOTE: This method overwrites existing properties
        :param custom_id: string or stringifyable value. 
        :param properties: user properties 
        :return: User
        """
        result = self.client.request('PATCH', '/identities/{}'.format(custom_id), {
            'properties': properties
        })
        return User(**result)

    def delete(self, custom_id):
        """
        Deletes a User object from remote using a custom_id
        :param custom_id: string or stringifyable value
        :return: Boolean
        """
        return self.client.request('DELETE', '/identities/{}'.format(custom_id))




