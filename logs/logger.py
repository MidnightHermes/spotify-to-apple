""" Houses the Logger class """
from constants import LOG_FORMAT


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
            self.__class__._initialized = True

    def log(self, level: str, message: str):
        """ Print log message and append log message to self.logs """
        log_message = LOG_FORMAT.format(level=level, message=message)
        print(log_message)
        self.logs.append(log_message)

    def get_logs(self) -> list[str]:
        """ Return self.logs """
        return self.logs
