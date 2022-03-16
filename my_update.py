from telegram import Update
from os import environ

THIS_BOT_ID = environ["THIS_BOT_ID"]

class MyUpdate():

    def __init__(self, update: Update):
        self.update = update
        self.chat_id = self.effective_chat.id

        if self.update.effective_chat.id:
            self.update.effective_chat.id = str(self.update.effective_chat.id)
        if self.update.message.from_user.id:
            self.update.message.from_user.id = str(self.update.message.from_user.id)


    def __getattr__(self, attr):
        return getattr(self.update, attr)


    def create_class(self):
        self.private_chat = self._is_private_chat()

        self.class_ = Telegram_Group(self.chat_id)
        if update.is_joined_chat():
            self.class_.read(default_write=True)
        else:
            self.class_.read()


    def _is_private_chat(self):
        return int(self.chat_id)>0

    
    def is_joined_chat(self):
        if self.my_chat_member:
            if self.my_chat_member.new_chat_member.user.id == THIS_BOT_ID:
                return self.my_chat_member.new_chat_member.status == "member"


    def is_left_chat(self):
        if self.my_chat_member:
            if self.my_chat_member.new_chat_member.user.id == THIS_BOT_ID:
                return self.my_chat_member.new_chat_member.status == "left"
