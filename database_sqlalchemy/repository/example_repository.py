# -*- coding: utf-8 -*-
__author__ = 'Gabriel Becker and Marco Borges'
__version__ = '0.1.0'

from sqlalchemy import func
from dbbase import DbResult
from .base_repository import Repository
from entity import ExampleEntity


class ExampleRepository(Repository):
   
    def __init__(self, db_session=None):
        if db_session is None:
            db_session = DbResult().get_new_connection()
        self._session = db_session
        super(ExampleRepository, self).__init__(db_session, ExampleEntity)

    def count(self):
        query = self._session.query(func.count(ExampleEntity.ID))
        return query.all()[0][0]

    def create(self, rule: ExampleEntity):
        return super(ExampleRepository, self).create_item(rule)

    def create_many(self, entities, return_defaults=False):
        self._session.bulk_save_objects(entities, return_defaults=return_defaults)
        self.commit()

    def delete(self, rule: ExampleEntity):
        self.delete_item(rule)

