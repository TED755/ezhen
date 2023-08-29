# import telebot
from core.ezhen_settings import EZHEN_CHAT_ID, EZHEN_TOKEN


class EzhenCore():
    def __init__(self):
        # self.ezhen = telebot.TeleBot(EZHEN_TOKEN)
        self.token = EZHEN_TOKEN
        self.chat_id = EZHEN_CHAT_ID
        # self.start_core()

    # def start_core(self):
    #     self.ezhen.infinity_polling(none_stop=True, interval=1)

    # def send_message(self, msg: str):
    #     self.ezhen.send_message(EZHEN_CHAT_ID, f"Здравствуйте. Я Эжень!!!"
    #                                            f"Вы написали: {msg}")

    # @self.ezhen.message_handler(func=lambda message: True)
    # def get_text_messages(message):
    #     request = message.text
