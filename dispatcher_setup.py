from os import environ
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext
from handlers import start_help


class MyUpdate(Update):
    def de_json(update, bot):
        update = Update.de_json(update, bot)
        if update.effective_chat.id:
            update.effective_chat.id = str(update.effective_chat.id)
        if update.message.from_user.id:
            update.message.from_user.id = str(update.message.from_user.id)
        return update

        
TELEGRAM_TOKEN = environ["TELEGRAM_TOKEN"]

bot = Bot(token=TELEGRAM_TOKEN)

dispatcher = Dispatcher(bot, None, workers=1)
dispatcher.add_handler(CommandHandler("start", start_help))