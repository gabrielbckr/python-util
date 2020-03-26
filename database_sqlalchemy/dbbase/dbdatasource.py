# -*- coding: utf-8 -*-
__author__ = 'Marco Borges'
__version__ = '0.2.1'

from smart_scheduler.std import DbBase, Logger, Singleton


class DbDataSource(DbBase, Singleton):

    def __init__(self):
        Logger().log.debug('DbDataSource Initializing.')
        self._raw_connection = None
        self._session_creator = None
        super(DbDataSource, self).__init__('agenda')

    def get_raw_connection(self):
        return super(DbDataSource, self).get_raw_connection()
