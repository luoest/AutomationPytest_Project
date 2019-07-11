import logging
import logging.config
import os

logFile = os.path.dirname(os.path.dirname(__file__)) + "/configFile/mylog.conf"
# os.startfile(logFile)

logging.config.fileConfig(logFile)
logger = logging.getLogger('case711')

def info(message):
    logger.info(message)

def debug(message):
    logger.debug(message)

def warning(message):
    logger.warning(message)
