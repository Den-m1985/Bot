from telebot import TeleBot, types


token = open("token.config", "r").read()

# Создаем экземпляр бота
bot = TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markupinline = types.InlineKeyboardMarkup()
    inlitem = types.InlineKeyboardButton(text='dsf', callback_data='tef')
    itembtn1 = types.KeyboardButton(text='Список вопросов 1')
    markup.add(itembtn1)
    markupinline.add(inlitem)
    bot.send_message(message.chat.id, "ВЫБЕРИТЕ КНОПКУ", reply_markup=markup)

def read_questions_file(file_name):
    file = open(file_name, "r", encoding='utf-8')
    questions = file.read().split('\n')
    print(questions)

# Обычный режим
@bot.message_handler(content_types=["text"])
def any_msg(message):
    NameLastName = ''
    name_of_plant = ''
    number_of_exp = ''
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="tef")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "сообщение из обычного режима", reply_markup=keyboard)

    if message.text == 'Список вопросов 1':
        qs = read_questions_file('Список вопросов 1.csv')
        bot.send_message(message.chat.id, qs[0])

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "tef":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="ответ")

bot.polling(none_stop=True)