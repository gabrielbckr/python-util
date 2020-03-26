# -*- coding: utf-8 -*-
__author__ = 'Marco Borges'
__version__ = '0.1.0'

import pandas as pd
from pandas.errors import ParserError
from smart_scheduler.std import Logger


def to_timestamp(x: str) -> pd.Timestamp:
    try:
        return pd.to_datetime(x)
    except ParserError:
        Logger().log.error('Error on %s conversion to Timestamp')
    return pd.NaT


def null_to_empty(x: str) -> str:
    return x if x not in ('NULL', 'UNREG') else ''
