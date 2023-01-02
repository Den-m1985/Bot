import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update, _):
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # для версии 13.x
    update.message.reply_text('Пожалуйста, выберите:', reply_markup=reply_markup)
    # для версии 20.x необходимо использовать оператор await
    # await update.message.reply_text('Пожалуйста, выберите:', reply_markup=reply_markup)


def button(update, _):
    query = update.callback_query
    variant = query.data

    # `CallbackQueries` требует ответа, даже если 
    # уведомление для пользователя не требуется, в противном
    #  случае у некоторых клиентов могут возникнуть проблемы. 
    # смотри https://core.telegram.org/bots/api#callbackquery.
    query.answer()
    # для версии 20.x необходимо использовать оператор await
    # await query.answer()

    # редактируем сообщение, тем самым кнопки 
    # в чате заменятся на этот ответ.
    query.edit_message_text(text=f"Выбранный вариант: {variant}")
    # для версии 20.x необходимо использовать оператор await
    # await query.edit_message_text(text=f"Выбранный вариант: {variant}")

def help_command(update, _):
    update.message.reply_text("Используйте `/start` для тестирования.")
    # для версии 20.x необходимо использовать оператор await
    # await update.message.reply_text("Используйте `/start` для тестирования.")


if __name__ == '__main__':
    # в версии 13.x создаются 2 объекта:
    # `updater` и диспетчер `app`
    updater = Updater("TOKEN")
    app = updater.dispatcher
    # для версии 20.x необходимо создать только 1 объект 
    # приложение через `Application.builder()`
    # app = Application.builder().token("TOKEN").build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler('help', help_command))

    # Запуск бота в версии 13.x происходит 
    # через объект `updater`
    updater.start_polling()
    updater.idle()

    # Запуск бота в версии 20.x 
    # app.run_polling()