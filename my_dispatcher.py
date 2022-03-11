from my_update import MyUpdate
from telegram.ext import Dispatcher


class MyDispatcher(Dispatcher):

    def __init__(self, *args, enable_private_messages=True, **kwargs):
        self.enable_private_messages = private_messages
        super().__init__(*args, **kwargs)   


    def process_update(self, update: MyUpdate):
        if not self.enable_private_messages and update.private_chat:
            return
        else:
            super().process_update(update)