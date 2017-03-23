# -*- coding: utf-8 -*-
from .base import Resource


class User(Resource):

    def create(self):
        return self.client.request('POST', '/users')

    def identify(self, user_id, custom_id, **properties):
        return self.client.request('POST', '/identify', data={
            'id': user_id,
            'custom_id': str(custom_id),
            'properties': properties
        })

    def create_and_identify(self, custom_id, **properties):
        result = self.create()
        permutive_id = result.get('id', None)
        if not permutive_id:
            raise ValueError('Id was not present in the response from Permutive API')

        return self.identify(permutive_id, custom_id, **properties)

    def get(self, custom_id):
        return self.client.request('GET', '/identities/{}'.format(custom_id))

    def update(self, custom_id, **properties):
        return self.client.request('PATCH', '/identities/{}'.format(custom_id), {
            'properties': properties
        })

    def delete(self, custom_id):
        return self.client.request('DELETE', '/identities/{}'.format(custom_id))




