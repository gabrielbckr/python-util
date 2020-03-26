# -*- coding: utf-8 -*-
__author__ = 'Gabriel Becker'
__version__ = '0.1.0'


class Meta(type):
    """Class to implement singleton type."""

    def __init__(cls, name, bases, dct):
        super(Meta, cls).__init__(name, bases, dct)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Meta, cls).__call__(*args, **kwargs)
        return cls.instance


class Singleton(object, metaclass=Meta):
    """Class to implement singleton."""

    def __init__(self):
        super(Singleton, self).__init__()
