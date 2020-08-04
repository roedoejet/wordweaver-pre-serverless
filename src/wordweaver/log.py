from loguru import logger
import sys

logger.add(sys.stderr, format="{level} {message}", level="INFO")
