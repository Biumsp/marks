from telegram import Update
from os import environ

THIS_BOT_ID = environ["THIS_BOT_ID"]

class MyUpdate(Update):

    def create_class(self):
        chat_id = self.effective_chat.id
        self.private_chat = self._is_private_chat()

        self.class_ = Telegram_Group(chat_id)
        if update.is_joined_chat():
            self.class_.read(default_write=True)
        else:
            self.class_.read()


    def de_json(request, bot):
        update = Update.de_json(request, bot)
        update.__class__ = MyUpdate

        if update.effective_chat.id:
            update.effective_chat.id = str(update.effective_chat.id)
        if update.message.from_user.id:
            update.message.from_user.id = str(update.message.from_user.id)
        return update


    def _is_private_chat(self):
        return int(chat_id)>0

    
    def is_joined_chat(self):
        if self.my_chat_member:
            if self.my_chat_member.new_chat_member.user.id == THIS_BOT_ID:
                return self.my_chat_member.new_chat_member.status == "member"


    def is_left_chat(self):
        if self.my_chat_member:
            if self.my_chat_member.new_chat_member.user.id == THIS_BOT_ID:
                return self.my_chat_member.new_chat_member.status == "left"
