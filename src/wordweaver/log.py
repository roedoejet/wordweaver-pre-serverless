import sys

from loguru import logger

logger.add(sys.stderr, format="{level} {message}", level="INFO")
