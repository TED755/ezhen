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
        message_words = message.text.split(' ')
        # print(user_id, chat_id)

        if not ezhen.is_me(message_words[0]):
            return

        try:
            action = ezhen.def_action(message_words[1:])
        except IndexError:
            ezhen_bot.send_message(chat_id, 'Что?')
            return
        answer = ezhen.do_action(action)

        ezhen_bot.send_message(chat_id, answer)

    ezhen_bot.infinity_polling(none_stop=True, interval=1)
