#необходимо установить библиотеку.
# pip install pyTelegramBotAPI
# разорвать соединение Ctrl C
import telebot
import codecs
import datetime


token = open("token.config", "r").read()

# Создаем экземпляр бота
bot = telebot.TeleBot(token)

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    with codecs.open('log', 'a', encoding='utf-8') as file:
        file.writelines(f'\n Chat {message.chat.id} Usrer: {message.from_user.first_name} Data: {datetime.datetime.now()} Message: {message.text}')
# Запускаем бота
bot.polling(none_stop=True, interval=0)