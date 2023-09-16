import telebot
from core.core import EzhenCore


def start_life():
    ezhen = EzhenCore()
    telebot.apihelper.ENABLE_MIDDLEWARE = True
    ezhen_bot = telebot.TeleBot(ezhen.token)

    @ezhen_bot.message_handler(func=lambda message: True)
    def get_text_messages(message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        # print(user_id, chat_id)
        request = message.text
        if ezhen.is_me(request):
            ezhen_bot.send_message(chat_id, f"вы написали {request}")

    ezhen_bot.infinity_polling(none_stop=True, interval=1)
