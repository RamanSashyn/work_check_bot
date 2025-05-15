# Work Check Bot

Telegram-бот, который следит за результатами проверки ваших работ на [dvmn.org](https://dvmn.org) и уведомляет вас в личные сообщения.

---

## Environment

Python 3.10+

---

## Requirements

Установите зависимости командой:

```bash
pip install -r requirements.txt
```

---

## Environment variables

Для работы проекта необходим файл `.env` со следующими переменными:

```env
DVMN_TOKEN=ваш_токен_девмана
BOT_TOKEN=токен_вашего_телеграм_бота
TG_CHAT_ID=ваш_чат_id
```

### How to get

* `DVMN_TOKEN` — получите [в личном кабинете dvmn.org](https://dvmn.org/api/docs/)
* `BOT_TOKEN` — создайте бота у [@BotFather](https://t.me/botfather)
* `TG_CHAT_ID` — напишите боту @userinfobot в Telegram

---

## Run

1. Клонируйте проект:

```bash
git clone https://github.com/your-username/work-check-bot.git
cd work-check-bot
```

2. Создайте виртуальное окружение и активируйте его:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. Запустите скрипт:

```bash
python main.py
```

---

## Notes

* Не публикуйте `.env` файл — добавьте его в `.gitignore`
* Проверки приходят через механизм long polling — скрипт работает в фоне, пока вы не остановите его
* Для запуска в облаке можно использовать PythonAnywhere, Heroku или сервер

---

Happy coding! 🚀
