from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from bot.db import Data


async def create_record(
        title: str,
        url: str,
        xpath: str,
        price: int,
        session_maker: sessionmaker
    ):
    async with session_maker() as session:
        async with session.begin():
            user = Data(
                title=title,
                url=url,
                xpath=xpath,
                price=price,
            )
            session.add(user)
