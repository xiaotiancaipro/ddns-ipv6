import atexit
import logging
import os
from logging.handlers import RotatingFileHandler

from utils.other import get_project_abspath


class Logger(object):

    def __init__(self, log_file=f"{get_project_abspath()}/logs/get-ipv6.log"):
        self.__log_file = log_file

    def get_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.__log_file)

        file_handler = RotatingFileHandler(log_file, maxBytes=50 * 1024 * 1024, backupCount=10)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(file_handler)

        atexit.register(file_handler.close)

        return logger
