from json import dumps as jsondumps
from os import environ
import logging
from httplogging import HttpHandler

# Settings -------------------------------------------------------------------------

LOGBOT_USERNAME = environ["LOGBOT_USERNAME"]
LOGBOT_PASSWORD = environ["LOGBOT_PASSWORD"]
TELEGRAM_CHATID = environ["TELEGRAM_CHATID"]  

APPNAME = "Marks"
LOGURL  = "https://us-central1-logbot-336012.cloudfunctions.net/log_bot"

CMDFORMAT  = '%(levelname)s - %(message)s'
DATEFORMAT = '%y/%m/%d - %H:%M:%S'
JSONFORMAT = {
    'time'      : '%(asctime)s',
    'appname'   : '%(name)s',
    'pathname'  : '%(pathname)s',
    'line'      : '%(lineno)d',
    'loglevel'  : '%(levelname)s',
    'message'   : '%(message)s'
}


# Handler Initialization -------------------------------------------------------------

# create a custom http logger handler
http_handler = HttpHandler(LOGURL, silent=True)

# set the http-handler level
http_handler.setLevel(logging.CRITICAL)

# create formatter - this formats the log messages accordingly
http_format = logging.Formatter(jsondumps(JSONFORMAT), datefmt=DATEFORMAT)

# add formatter to custom http handler
http_handler.setFormatter(http_format)

# add credentials 
http_handler.setCredentials(LOGBOT_USERNAME, LOGBOT_PASSWORD)

# set telegram chat_id
http_handler.setTelegramChatId(TELEGRAM_CHATID)

# Logging settings -----------------------------------

log_level = logging.ERROR
logging.basicConfig(format=CMDFORMAT, datefmt=DATEFORMAT, level=log_level)


# Create logger instance -----------------------------------

logger = logging.getLogger(APPNAME)
logger.addHandler(http_handler) 