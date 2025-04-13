""" Houses the Logger class """
from time import sleep
from sys import float_info

from constants import LOG_FORMAT, LOG_FILE_PATH


class Logger:
    """ Handles all logging logic """

    _instance = None
    _initialized = False

    def __new__(cls):
        """ Ensure Singleton, only one instance may exist """
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not self.__class__._initialized:
            self.logs = []
            self.log_file = open(LOG_FILE_PATH, 'w', encoding='utf8')
            self.__class__._initialized = True

    def log(self, level: str, message: str):
        """ Print log message and append log message to self.logs """
        log_message = LOG_FORMAT.format(level=level, message=message)
        sleep(float_info.min)
        print('\033[K' + log_message, end='' if level == "INFO" else '\n')
        self.logs.append(log_message)
        self.log_file.write(log_message)

    def get_logs(self) -> list[str]:
        """ Return self.logs """
        return self.logs

    def get_most_recent_log(self) -> str:
        """ Return self.logs """
        return self.logs[-1]

    def __del__(self):
        self.log_file.close()
