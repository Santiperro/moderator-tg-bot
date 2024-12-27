import json
import logging

from exceptions.exceptions import MessageNotFoundError


class MessageLoader:
    _instance = None

    def __new__(cls, file_path):
        if cls._instance is None:
            cls._instance = super(MessageLoader, cls).__new__(cls)
            cls._instance.file_path = file_path
            cls._instance.messages = cls._instance.load_messages()
        return cls._instance


    def __getitem__(self, key):
        return self.messages.get(key, self.messages["error_message"])
    
    def load_messages(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)


messages_loader = MessageLoader('texts/messages.json')
