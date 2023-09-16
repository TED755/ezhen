# import telebot
import json
from core.ezhen_settings import EZHEN_CHAT_ID, EZHEN_TOKEN
from core.ezh_except import EzhException


class EzhenCore():
    def __init__(self):
        # self.ezhen = telebot.TeleBot(EZHEN_TOKEN)
        self.token = EZHEN_TOKEN
        self.chat_id = EZHEN_CHAT_ID
        try:
            with open('core/ezhen_vocabluary.json', 'r') as vocabluary:
                self.vocabluary = json.load(vocabluary)
        except FileNotFoundError:
            raise EzhException(message='Не найден словарь Эженя')
        # self.start_core()

    def is_me(self, message: str) -> bool:
        split_string_arr = message.split(' ')
        for my_name in self.vocabluary['me']:
            if my_name in split_string_arr[0].lower():
                return True
        return False

    # def start_core(self):
    #     self.ezhen.infinity_polling(none_stop=True, interval=1)

    # def send_message(self, msg: str):
    #     self.ezhen.send_message(EZHEN_CHAT_ID, f"Здравствуйте. Я Эжень!!!"
    #                                            f"Вы написали: {msg}")

    # @self.ezhen.message_handler(func=lambda message: True)
    # def get_text_messages(message):
    #     request = message.text
