import os
import asyncio
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.redis import RedisStorage
from sqlalchemy import URL

from bot.handlers import register_user_commands
from bot.settings import bot_commands, redis
from bot.db import create_async_engine, get_session_maker


load_dotenv()


TELEGRAM_TOKEN = os.getenv('TOKEN')


async def main():
    logging.basicConfig(level=logging.DEBUG)
    commands_for_bot = []

    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    dp = Dispatcher(storage=RedisStorage(redis=redis))
    bot = Bot(TELEGRAM_TOKEN)
    await bot.set_my_commands(commands=commands_for_bot)

    postgres_url = URL.create(
        drivername="postgresql+asyncpg",
        username=os.getenv("POSTGRES_USER"),
        host='127.0.0.1',
        database=os.getenv("POSTGRES_DB"),
        port=os.getenv("POSTGRES_PORT"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)

    register_user_commands(dp)

    ####
    # await redis.flushdb()

    await dp.start_polling(bot, session_maker=session_maker)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt,):
        print('Bot stoped')
