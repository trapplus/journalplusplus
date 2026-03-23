import sys
from loguru import logger


def setup_logger(log_level: str) -> None:
    logger.remove()

    fmt = (
        "<green>{time:HH:mm:ss}</green> | "
        "<level>{level:<8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )

    # console
    logger.add(sys.stdout, format=fmt, level=log_level, colorize=True)

    # file — rotation каждые 10MB, хранить 7 дней
    logger.add(
        "logs/journal.log",
        format=fmt,
        level=log_level,
        rotation="10 MB",
        retention="7 days",
        colorize=False,
        encoding="utf-8",
    )


__all__ = ["logger", "setup_logger"]