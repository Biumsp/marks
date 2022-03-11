from telegram.ext import CallbackContext
from telegram import Update
from telegram import ParseMode
from logging_setup import logger
from telegram_group import Telegram_Group
from telegram_user import Telegram_User


GROUP_HELP  = "Group Help Message" 

def start_help(update: Update, context: CallbackContext):

    chat_id = update.effective_chat.id
    context.bot.sendMessage(chat_id=chat_id,
                            text=update,
                            parse_mode=ParseMode.HTML)