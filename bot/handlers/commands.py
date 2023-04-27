from typing import Any
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.methods import SendMessage

from sqlalchemy.orm import sessionmaker

import bot.settings as sett


async def start(
    message: types.Message,
    ):
    """
    Хендлер для команды /start
    :param message:
    """
    await message.answer(
        sett.START_MESSAGE
    )


# async def dialogue_list(
#         message: types.Message,
#         state: FSMContext,
#         session_maker: sessionmaker,
#     ):
#     await state.clear()
#     user_id = message.from_user.id
#     dial_list = await get_user_dialogues(
#         user_id,
#         session_maker
#         )
#     await message.answer(
#         text='Ваши диалоги',
#         reply_markup=gen_dialogues_kb(dial_list)
#         )
    



# функция выхода из машины состояний
# async def censel_hendler(
#         message: types.Message,
#         state: FSMContext,
#         ):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.clear()
    # return await SendMessage(
    #     text='Дейстаия отменены',
    #     chat_id=message.from_user.id,
    #     reply_markup=START_BOARD)
