# import telebot
import json
from core.ezhen_settings import EZHEN_TOKEN
from core.ezh_except import EzhException


class EzhenCore():
    def __init__(self):
        self.token = EZHEN_TOKEN
        try:
            with open('core/ezhen_vocabluary.json', 'r') as vocabluary:
                self.vocabluary = json.load(vocabluary)
        except FileNotFoundError:
            raise EzhException(message='Не найден словарь Эженя')

    def is_me(self, first_word: str) -> bool:
        for my_name in self.vocabluary['me']:
            if my_name in first_word.lower():
                return True
        return False

    def def_action(self):
        ...

    def action(self):
        ...
