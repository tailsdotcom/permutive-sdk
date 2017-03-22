Permutive SDK
--------

Instructions::

    >>> import permutive
    >>> permutive = Permutive('<private_api_key>')

    Users:
    Fetch an existing user by using a custom_id:
    >>> permutive.users.get('dnshio')
    {
         u'id': u'12345',
         u'properties': {u'email': u'test@example.com'},
         u'updated': u'2017-03-22T14:59:06.828Z',
         u'user_id': u'4041dac0-9f23-4b72-96fd-8154e7c5f4ef'
    }
    Use the `id` returned when sending events

    Create and identify a user:
    >>> permutive.users.create_and_identify('dnshio', email='dnshio@example.com', gender='male')

    Events:
    Track an event
    >>> response = permutive.users.get('dnshio')
    >>> user_id = response.get('id')
    >>> permutive.events.track('CustomerSubscribed', user_id, product_type='digital', active=True)
