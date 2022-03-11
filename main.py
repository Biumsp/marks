from os import environ
from telegram import Bot
from telegram import ParseMode
from dispatcher_setup import bot, dispatcher
from my_update import MyUpdate
from logging_setup import logger

def marks(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    if request.method == "POST":

        try:
            request_json = request.get_json(force=True)

            update = MyUpdate.de_json(request_json, bot)
            update.create_class()

            dispatcher.process_update(update)

            return "200"

        except:
            logger.critical("400 Bad Request")
            return "400"
                    
    return "The bot is active"