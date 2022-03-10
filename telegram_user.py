class Telegram_User():

    def __init__(self, chat_id):
        self.chat_id = chat_id

    def __eq__(self, other: str):

        if type(other) == str:
            return self.chat_id == key
        
        if type(other) == Telegram_User:
            return self.chat_id == other.chat_id