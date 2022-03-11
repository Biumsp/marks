from os import environ
from telegram import Bot
from telegram.ext import CommandHandler, CallbackContext
from handlers import start_help
from telegram_group import Telegram_Group
from my_dispatcher import MyDispatcher


TELEGRAM_TOKEN = environ["TELEGRAM_TOKEN"]


bot = Bot(token=TELEGRAM_TOKEN)

dispatcher = MyDispatcher(bot, None, workers=1, enable_private_messages=False)
dispatcher.add_handler(CommandHandler("start", start_help))