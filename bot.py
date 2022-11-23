#необходимо установить библиотеку.
# pip install pyTelegramBotAPI
# разорвать соединение Ctrl C
import telebot


token = open("token.config", "r").read()

# Создаем экземпляр бота
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def lalala(m, res=False):
    bot.send_message(m.chat.id, 'message.text')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'вы написали')
    
# run
bot.polling(non_stop=True, interval=0)
