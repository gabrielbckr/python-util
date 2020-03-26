# -*- coding: utf-8 -*-
__author__ = 'Marco Borges'
__version__ = '0.1.0'

from smart_scheduler.std import DbBase, Logger, Singleton


class DbResult(DbBase, Singleton):

    def __init__(self):
        Logger().log.debug('DbSource Initializing.')
        self._raw_connection = None
        self._session_creator = None
        super(DbResult, self).__init__('result')

    def get_new_connection(self):
        return self.get_session_maker(False, True)()
