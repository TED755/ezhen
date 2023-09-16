import telebot
from core.core import EzhenCore


def start_life():
    ezhen = EzhenCore()
    telebot.apihelper.ENABLE_MIDDLEWARE = True
    ezhen_bot = telebot.TeleBot(ezhen.token)

    @ezhen_bot.message_handler(func=lambda message: True)
    def get_text_messages(message):
        request = message.text
        if ezhen.is_me(request):
            ezhen_bot.send_message(ezhen.chat_id, f"вы написали {request}")

    ezhen_bot.infinity_polling(none_stop=True, interval=1)
