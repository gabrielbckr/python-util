# -*- coding: utf-8 -*-
__author__ = 'Gabriel Becker and Marco Borges'
__version__ = '0.3.0'

from sqlalchemy.sql import text

TEST_QUERY = text("""
SELECT 1
""")

from .singleton import Singleton
from .logger import Logger
from .configuration import Config
from dbbase import DbBase
from .dbdatasource import DbDataSource
from .dbresult import DbResult
from .string_conversions import null_to_empty, to_timestamp
