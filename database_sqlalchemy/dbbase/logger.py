# -*- coding: utf-8 -*-
__author__ = 'Gabriel Becker'
__version__ = '0.1.0'

import logging
from smart_scheduler.std import Singleton

class Logger(Singleton):

    def __init__(self):
        self.log = logging.getLogger('IHP_Smart_Scheduler')
        self.log.setLevel(logging.DEBUG)
        # add console
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        self.log.addHandler(console)
        super(Logger, self).__init__()
