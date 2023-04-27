import io
import pandas as pd
from typing import Any
from aiogram import Bot, types
from aiogram.methods import SendMessage

from sqlalchemy.orm import sessionmaker

import bot.settings as sett
from ._tools import processing_exel_data


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


async def file_processing(
        message: types.Message,
        session_maker: sessionmaker,
        **data: dict[str, Any],
    ):
    nsg = await SendMessage(
        text='Обработка...',
        chat_id=message.from_user.id,
    )
    file_id = message.document.file_id
    bot: Bot = data['bot']
    file = await bot.get_file(file_id)
    tg_file_path = file.file_path
    file: io.BytesIO = await bot.download_file(tg_file_path)
    file.seek(0)
    df = pd.read_excel(file, 'Sheet1')

    try:
        avf_price = await processing_exel_data(df, session_maker)
    except IndexError:
        await nsg.edit_text(
            f'Один из сайтов отказал в доступе к своей странице'
        )
        return
    
    await nsg.edit_text(
        f'Средняя цена товара из вашего списка равна {avf_price}'
    )
    