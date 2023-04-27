Тестовое задание в компанию Technesis.


Использовались технологии:

Python3.10, Aiogram 3.0.0b7, SQLAlchemy 2, PostgresQL


## Инструкции по установке

## ***- Клонируйте репозитори******й:***

```
https://github.com/RussianPostman/Technesis_test_wor
```

Cоздайте и заполните .env файл в директории infra

```
TOKEN=*** - токен вашего телеграм бота

POSTGRES_USER=root
POSTGRES_PASSWORD=ubnfhf
POSTGRES_HOST=ppostgres.Technesis
POSTGRES_DB=Technesis_db
POSTGRES_PORT=8764
```

## - *Перейдите в директорию /infra и запустите контейнеры*

```
cd infra
docker-compose up -d --build
```

Проверить бота можно по ссылке https://t.me/Russian_postman_dev_bot
