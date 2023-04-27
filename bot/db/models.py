from sqlalchemy.orm import mapped_column, Mapped

from bot.db.base import BaseModel


class Data(BaseModel):
    """
    args:
        id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
        title: Mapped[str]
        url: Mapped[str]
        xpath: Mapped[str]
        data: Mapped[str]
    """
    __tablename__ = 'pas_data'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    url: Mapped[str]
    xpath: Mapped[str]
    data: Mapped[str]

    def __str__(self) -> int:
        return f'User: {self.user_id}'

    def __repr__(self):
        return self.__str__()
