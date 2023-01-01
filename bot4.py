from telebot import TeleBot, types

token = open("token.config", "r").read()

# Создаем экземпляр бота
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #btn1 = types.KeyboardButton("👋 Поздороваться")
    info = types.KeyboardButton("❓ INFO")
    abc = types.KeyboardButton("Действие")
    markup.add(info, abc)
    bot.send_message(message.chat.id, text="Привет user".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "❓ INFO"):
        bot.send_message(message.chat.id, text="Информация")
    elif(message.text == "Действие"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Добавить новый контакт?")
        btn2 = types.KeyboardButton("Вывести на экран контакты?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif message.text == "Добавить новый контакт?":
        bot.send_message(message.chat.id, text="Ипалит")

bot.polling(none_stop=True, interval=0)