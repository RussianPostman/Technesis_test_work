import os
from httpx import Timeout
from dotenv import load_dotenv
from aioredis import Redis


load_dotenv()


redis = Redis()

bot_commands = (
    ("start", "Начало работы с ботом"),
)

START_MESSAGE = (
    'Здравствуйте, пришлите список сайтов для парсинга цен в формате '
    + 'excel таблицы с полями: \n'
    + 'title - название \nurl - ссылка на сайт источник \nxpath - путь к элементу с ценой')
