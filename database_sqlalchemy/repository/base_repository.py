# -*- coding: utf-8 -*-
__author__ = 'Marco Borges'
__version__ = '0.1.1'

from sqlalchemy.orm import Session


class Repository(object):

    def __init__(self, db_session: Session, obj_class: object):
        assert db_session is not None
        assert isinstance(db_session, Session)
        assert obj_class is not None

        self.db_session = db_session
        self.obj_class = obj_class

    def create_item(self, item):
        if item is not None:
            self.db_session.add(item)
            self.commit()
        return item

    def commit(self):
        try:
            self.db_session.commit()
        except Exception:
            self.db_session.rollback()

    def delete_item(self, item):
        item.is_valid = False
        self.db_session.commit()

    def expire(self):
        self.db_session.expire_all()

    def expunge(self):
        self.db_session.expunge_all()

    def get_valid_item(self, object_valid_field, object_key_field, object_id):
        return self.db_session.query(self.obj_class).filter(object_valid_field).\
            filter(object_key_field == object_id).first()

    def get_item(self, object_key_field, object_id):
        return self.db_session.query(self.obj_class).filter(object_key_field == object_id).first()

    def get_item_by_prop(self, object_valid_field, prop, value):
        return self.db_session.query(self.obj_class).filter(object_valid_field).filter(prop == value)

    def query(self, *restrictive_clauses):
        query = self.db_session.query(self.obj_class)
        for clause in restrictive_clauses:
            query = query.filter(clause)
        return query
