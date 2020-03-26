# -*- coding: utf-8 -*-
__author__ = 'Gabriel Becker'
__version__ = '0.1.1'

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .example_table_entity import ExampleEntity
