from json import dumps, loads
from logging_setup import logger
from google.cloud import storage
from os import environ


class Database:

    def __init__(self, bucket_name, file_name):
        self.bucket_name = bucket_name
        self.file_name   = file_name
        

    def read():
        client = storage.Client()
        bucket = client.bucket(self.bucket_name)
        blob   = bucket.blob(self.file_name)

        content   : bytes = blob.download_as_bytes()
        data_str  : str   = content.decode("utf-8") 
        data_dict : dict  = loads(data_str)

        return data_dict


    def write(self, data: dict):
        client = storage.Client()
        bucket = client.bucket(self.bucket_name)
        blob   = bucket.blob(self.file_name)

        blob.upload_from_string(dumps(data))