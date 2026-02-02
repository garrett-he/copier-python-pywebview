"""Logging configuration."""

import sys
from pathlib import Path

from loguru import logger


def setup_logging(debug: bool, log_file: Path) -> None:
    """Configure loguru based on runtime mode.

    In debug mode, all logs go to stdout (DEBUG+) and stderr (ERROR+).
    In production, all logs go to a rotating file with [LEVEL] tags.

    Args:
        debug: Whether to use debug (console) or production (file) logging.
        log_file: Path to the log file (only used when debug=False).
    """
    logger.remove()

    fmt = '[{time:HH:mm:ss}][{level}] {message}'

    if debug:
        logger.add(
            sys.stdout,
            level='DEBUG',
            format=f'<green>{fmt}</green>',
        )
        logger.add(
            sys.stderr,
            level='ERROR',
            format=f'<red>{fmt}</red>',
        )
    else:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        logger.add(
            log_file,
            level='INFO',
            rotation='1 MB',
            retention='7 days',
            format=fmt,
        )
