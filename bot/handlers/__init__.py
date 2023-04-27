__all__ = ['register_user_commands']

from aiogram import Router, F
from aiogram.filters.command import CommandStart
from bot.handlers.commands import start


def register_user_commands(router: Router) -> Router:
    """
    Зарегистрировать хендлеры пользователя
    :param router:
    """
    router.message.register(start, CommandStart())

