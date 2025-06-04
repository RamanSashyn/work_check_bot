# Work Check Bot

Telegram-бот, который следит за результатами проверки ваших работ на [dvmn.org](https://dvmn.org) и уведомляет вас в личные сообщения.

---

## Environment

- Python 3.8+
- виртуальное окружение (`venv`)
- зарегистрированный бот в Telegram

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
git clone git@github.com:your-username/work-check-bot.git
cd work-check-bot
```

2. Создайте виртуальное окружение и активируйте его:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. Запустите скрипт:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Установите зависимости:

```bash
pip install -r requirements.txt
```
---

5. Запуск:
```bash
python3 main.py
```

6. Запуск на сервере через systemd:
   1. Поместите проект в /opt/work_check_bot
   2. Создайте юнит-файл /etc/systemd/system/work_check_bot.service:
   3. Запустите:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable work_check_bot
   sudo systemctl start work_check_bot
   ```

## Notes

* Не публикуйте `.env` файл — добавьте его в `.gitignore`
* Проверки приходят через механизм long polling — скрипт работает в фоне, пока вы не остановите его
* Для запуска в облаке можно использовать PythonAnywhere, Heroku или сервер

---

Happy coding! 🚀
