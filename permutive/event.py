# -*- coding: utf-8 -*-
from .util import none_default_namedtuple
from .base import Resource

Event = none_default_namedtuple('Event', 'name, user_id, id, properties, time')


class EventResource(Resource):

    def track(self, event_name, user_id, **properties):
        """
        Records an event in Permutive API
        
        https://developer.permutive.com/v1.1/reference#record-an-event
        :param event_name: String name of the event, e.g. EmailSubscription
        :param user_id: String - Permutive user_id
        :param properties: keyword arguments representing event properties to be sent
        :return: dict 
        """
        result = self.client.request('POST', '/events', data={
            'user_id': user_id,
            'name': event_name,
            'properties': properties
        })
        return Event(**result)

    def get(self, user_id, start=None, end=None):
        """
         Fetch events for a given user_id
        :param user_id: 
        :param start: (optional) datetime
        :param end: (optional) datetime
        :return: Generator that return Event objects
        """
        data = {'user_id': user_id}
        if start:
            data['start'] = start.isoformat()
        if end:
            data['end'] = end.isoformat()

        result = self.client.request('GET', '/events', data=data)

        for event in result:
            yield Event(**event)
