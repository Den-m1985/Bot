import telebot
import config

bot = telebot.TeleBot(config.TOKEN)
#bot = telebot.TeleBot('5731423337:AAGr97IwINO9S7VXf20PIx7JpGjU-IZzXow')

@bot.message_handler(commands=["start"])
def lalala(m, res=False):
    bot.send_message(m.chat.id, 'message.text')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'вы написали')
    
# run
bot.polling(non_stop=True, interval=0)
