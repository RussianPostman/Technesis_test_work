import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKEN')

bot_commands = (
    ("start", "Начало работы с ботом"),
)

START_MESSAGE = (
    'Здравствуйте, пришлите список сайтов для парсинга цен в формате '
    + 'excel таблицы с полями: \n'
    + 'title - название \nurl - ссылка на сайт источник \nxpath - путь к элементу с ценой')
