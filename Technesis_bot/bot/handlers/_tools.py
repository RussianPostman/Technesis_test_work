import requests
import pandas as pd
from lxml import html
from statistics import mean
from sqlalchemy.orm import sessionmaker
from bs4 import BeautifulSoup

from bot.db import create_record


async def processing_exel_data(
        file: pd.DataFrame,
        session_maker: sessionmaker,
    ) -> int:
    url_list = file['url'].to_list()
    xpath_list = file['xpath'].to_list() 
    title_list = file['title'].to_list()
    count = 0
    stop = len(url_list)
    price_list = []

    while count < stop:
        page = requests.get(url_list[count])
        tree = html.fromstring(page.text) 
        elements: list[str] = tree.xpath(xpath_list[count])
        if len(elements) > 0:
            if type(elements[0]) == html.HtmlElement:
                html_data = elements[0].text.strip()
                price = int(''.join(i for i in html_data if i.isdigit()))
                price_list.append(price)
            else:
                html_data = elements[0].strip()
                price = int(''.join(i for i in html_data if i.isdigit()))
                price_list.append(price)
            
            await create_record(
                title_list[count],
                url_list[count],
                xpath_list[count],
                price,
                session_maker
                )
        count += 1
    return round(mean(price_list), 1)

