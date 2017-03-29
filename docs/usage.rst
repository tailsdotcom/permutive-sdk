=====
Usage
=====

To use Permutive SDK in a project::

    from permutive import Permutive

    permutive = Permutive(<YOUR_PRIVATE_KEY>)

Dispatch an event to Permutive::

    permutive.events.track('EmailSignup', customer.permutive_id, email_frequency=7)

Create user::

    permutive.users.create()


