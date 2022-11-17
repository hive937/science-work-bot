from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import ReplyKeyboardMarkup
import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
URL = 'https://api.thecatapi.com/v1/images/search'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def get_new_image():
    try:
        response = requests.get(URL).json()
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    random_cat = response[0].get('url')
    return random_cat


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/continue']], resize_keyboard=True)
    context.bot.send_photo(chat.id, 'http://www.alumnirussia.org/upload/partners/original_400bee9fa830a2591727f7fd71d8ef0e.png')
    context.bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {format(name)}. Я бот, помогающий студентам Финансового'
             f' Университета интересно проводить свое время в туризме. Нажми'
             f' на кнопку чтобы продолжить.',
        reply_markup=button
    )


def where_to_go(update, context):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['Туризм в Москве'], ['Туризм вне Москвы или области']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text=f'Поведай, куда бы ты хотел отправиться.',
        reply_markup=button
    )


def main():
    updater = Updater(token=token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('continue', where_to_go))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
