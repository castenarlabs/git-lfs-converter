import sys
import logging
from logging.handlers import MemoryHandler


class Logger(object):
    def __init__(self):
        #sys.stderr = sys.stdout
        self.terminal = sys.stdout
        #self.terminal = sys.stderr
        self.log = open("yourapp.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
            # this flush method is needed for python 3 compatibility.
            # this handles the flush command by doing nothing.
            # you might want to specify some extra behavior here.
        pass

    sys.stderr = sys.stdout
