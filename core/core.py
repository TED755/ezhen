# import telebot
import json
from core.ezhen_settings import EZHEN_TOKEN
from core.ezh_except import EzhException


class EzhenCore():
    def __init__(self):
        self.token = EZHEN_TOKEN
        # self.chat_id = EZHEN_CHAT_ID
        try:
            with open('core/ezhen_vocabluary.json', 'r') as vocabluary:
                self.vocabluary = json.load(vocabluary)
        except FileNotFoundError:
            raise EzhException(message='Не найден словарь Эженя')

    def is_me(self, message: str) -> bool:
        split_string_arr = message.split(' ')
        for my_name in self.vocabluary['me']:
            if my_name in split_string_arr[0].lower():
                return True
        return False
