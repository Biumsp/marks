from database import Database
from os import environ

BUCKET_NAME = environ["BUCKET_NAME"]

class Telegram_Group():

    def __init__(self, chat_id, members: list=[]):
        self.chat_id = chat_id
        self.members = members

        self.database = Database(BUCKET_NAME, self.chat_id)


    def __getitem__(self, key: str):
        assert (isinstance(key, str),
                f"expected str, got: {type(key)}")

        for m in self.members:
            if m == key:
                return m


    def __str__(self):
        return str(self.to_dict())


    def to_dict(self):
        return {m.chat_id: m for m in self.members}


    def add_member(self, member_id):
        self.members.append(member)


    def remove_member(self, member_id):
        self.members = [m for m in self.members if m != member_id]


    def save(self):
        self.database.write(self.to_dict())


    def read(self):
        self.members = list(self.database.read().values())