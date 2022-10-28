import telebot
#import config

#bot = telebot.TeleBot(config.TOKEN)
bot = telebot.TeleBot('5731423337:AAGr97IwINO9S7VXf20PIx7JpGjU-IZzXow')

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)
    
# run
bot.polling(non_stop=True)
