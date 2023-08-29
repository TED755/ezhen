import telebot
from ezhen_settings import EZHEN_CHAT_ID, EZHEN_TOKEN


bot = telebot.TeleBot(EZHEN_TOKEN)


@bot.message_handler(func=lambda message: True)
def get_text_messages(message):
    request = message.text

    bot.send_message(EZHEN_CHAT_ID, f"Здравствуйте. Я Эжень!!!"
                                    f"Вы написали: {request}")


bot.infinity_polling(none_stop=True, interval=1)
