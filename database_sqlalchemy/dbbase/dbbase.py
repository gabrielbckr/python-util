# -*- coding: utf-8 -*-
__author__ = 'Marco Borges'
__version__ = '0.3.1'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema
from sqlalchemy.engine.url import make_url
from smart_scheduler.entity import Base
from smart_scheduler.std import TEST_QUERY, Config, Logger


class DbBase(object):

    def __init__(self, database: str, db_schema: str = 'dbo'):
        assert isinstance(database, str)
        assert isinstance(db_schema, str)
        Logger().log.debug('DbBase Initializing.')
        self._session_creator = None
        self._raw_connection = None
        self._database = database
        self._db_schema = db_schema

    @staticmethod
    def check_connection(session) -> bool:
        return session.execute(TEST_QUERY).first()[0] == 1

    @staticmethod
    def generate_session_maker(conn_string: str, schema: str, create_schema: bool = False, create_tables: bool = True):
        try:
            engine = create_engine(conn_string, convert_unicode=True)
            if create_schema:
                engine.execute(CreateSchema(schema))
            if create_tables:
                Base.metadata.create_all(engine)
            session_creator = sessionmaker(bind=engine)

            return session_creator, engine.raw_connection()
        except Exception as exp:
            error_msg = f'Database access error {str(exp)}.'
            Logger().log.error(f'Database access error {str(exp)}.')
            raise IOError(error_msg)

    def get_connection_string(self):
        config = Config()
        connection_string = config.get_db_connection_string(self._database)
        if connection_string:
            return make_url(connection_string)

    def get_session_maker(self, create_schema: bool = False, create_tables: bool = False):
        Logger().log.info(f'Accessing data session of {self._database}.')
        if self._session_creator is None:
            Logger().log.info(f'Creating session maker of {self._database}.')
            self._session_creator, self._raw_connection = DbBase.generate_session_maker(
                self.get_connection_string(),
                self._db_schema,
                create_schema,
                create_tables
            )
            try:
                session = self._session_creator()

                if not DbBase.check_connection(session):
                    error_msg = 'Database query error'
                    Logger().log.error(error_msg)
                    raise IOError(error_msg)
                session.close()
            except Exception as exp:
                error_msg = f'Database access error {str(exp)}'
                Logger().log.error(error_msg)
                raise IOError(error_msg)
        return self._session_creator

    def get_new_connection(self):
        Logger().log.info(f'Accessing {self._database} new connection.')
        return self.get_session_maker()()

    def get_raw_connection(self):
        Logger().log.info(f'Accessing {self._database} raw connection.')
        if self._raw_connection is None:
            self.get_session_maker()
        return self._raw_connection
