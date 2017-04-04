import collections

import datetime


def none_default_namedtuple(typename, field_names, default_values=()):
    """
    Helper function for defining a namedtuple with defined defaults 
    """
    T = collections.namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, collections.Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T


def normalise_to_isoformat(val):
    if isinstance(val, dict):
        d = {}
        for k, v in val.iteritems():
            d[k] = normalise_to_isoformat(v)
            return d
    return val.isoformat() if isinstance(val, (datetime.datetime, datetime.date)) else val
