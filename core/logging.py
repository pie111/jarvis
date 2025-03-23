from loguru import logger
import sys

logger.remove()
logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")
logger.add("app.log", rotation="500 MB", level="DEBUG")