from telegram import Bot
import requests

bot = Bot(token='5775065280:AAHuc1DYHozb6X9oSA2I2i4yQE8OwXVQjxw')
URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = 1324611166

response = requests.get(URL).json()
random_cat_url = response[0].get('url')

bot.send_photo(chat_id, random_cat_url)
