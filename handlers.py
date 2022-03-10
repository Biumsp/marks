from telegram.ext import CallbackContext
from telegram import Update
from telegram import ParseMode
from logging_setup import logger
from telegram_group import Telegram_Group
from telegram_user import Telegram_User


GROUP_HELP  = "Group Help Message" 


def is_private_chat(update: Update):
    return int(update.effective_chat.id) > 0


def start_help(update: Update, context: CallbackContext):

    chat_id = update.effective_chat.id

    if is_private_chat(update):
        return
    else:
        # context.bot.sendMessage(chat_id=chat_id,
        #                         text=GROUP_HELP,
        #                         parse_mode=ParseMode.HTML)

        context.bot.sendMessage(chat_id=chat_id,
                                 text=update,
                                 parse_mode=ParseMode.HTML)