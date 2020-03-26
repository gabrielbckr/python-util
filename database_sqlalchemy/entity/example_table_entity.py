# -*- coding: utf-8 -*-
__author__ = 'Gabriel Becker and Marco Borges '
__version__ = '0.2.0'

import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mssql import  DATETIME2, INTEGER, TINYINT, FLOAT, BINARY
from smart_scheduler.entity import Base, DateEntity, ExamGroupEntity


class ExampleEntity(Base):
    __tablename__ = 'TABLENAME'

    ID = Column('TABLEATT1', INTEGER, primary_key=True, autoincrement=True, nullable=False)
    another_table_key = Column('TABLEATT2_WITH_FOREIGN_KEY', INTEGER, ForeignKey(ExamGroupEntity.id_group))
    att_float = Column('TABLEATT3', FLOAT)
    date = Column('TABLEATT4', DATETIME2, nullable=False, default=dt.datetime.utcnow)
    is_valid = Column('TABLEATT5', BINARY, default=True, nullable=False)
    global_key = Column('TABLEATT6', TINYINT)

    def __str__(self) -> str:
        return f'<{self.ID}>'

    def __repr__(self):
        return self.__str__()
