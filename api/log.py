import logging
import os
from logging import Logger

from concurrent_log_handler import ConcurrentRotatingFileHandler


def setup_logger(
        level: int = logging.INFO,
        max_bytes: int = 1024 * 1024 * 100,
        backup_count=30
) -> Logger:
    log_file_path = os.path.join(os.getcwd(), "logs")
    log_file = os.path.join(log_file_path, "ddns-ipv6.log")
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s")
    handler = ConcurrentRotatingFileHandler(log_file, "a", max_bytes, backup_count)
    handler.setFormatter(formatter)
    custom_logger = logging.getLogger(__name__)
    custom_logger.setLevel(level)
    custom_logger.addHandler(handler)
    return custom_logger


logger = setup_logger()
