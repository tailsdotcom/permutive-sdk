from permutive.base import Resource


class Event(Resource):

    def track(self, event_name, user_id, **properties):
        """
        Records an event in Permutive API
        
        https://developer.permutive.com/v1.1/reference#record-an-event
        :param event_name: String name of the event, e.g. EmailSubscription
        :param user_id: String - Permutive user_id
        :param properties: keyword arguments representing event properties to be sent
        :return: dict 
        """
        return self.client.request('POST', '/events', data={
            'user_id': user_id,
            'name': event_name,
            'properties': properties
        })
