import logging
from logging import Logger
from concurrent_log_handler import ConcurrentRotatingFileHandler
import os


def setup_logger(
        log_file: str,
        level: int = logging.INFO,
        max_bytes: int = 1024 * 1024 * 100,
        backup_count=30
) -> Logger:
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s")
    handler = ConcurrentRotatingFileHandler(log_file, "a", max_bytes, backup_count)
    handler.setFormatter(formatter)
    custom_logger = logging.getLogger(__name__)
    custom_logger.setLevel(level)
    custom_logger.addHandler(handler)
    return custom_logger


logger = setup_logger(log_file="../logs/ipv6-address-acquisition.log")
