# Work Check Bot

Этот бот следит за проверками ваших работ на [dvmn.org](https://dvmn.org/) и присылает уведомления в Telegram.

## Как запустить

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/your-username/work-check-bot.git
   cd work-check-bot
   ```

2. Создайте виртуальное окружение (esli не сделано):

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` и добавьте туда:

   ```env
   DVMN_TOKEN=ваш_токен_девмана
   TELEGRAM_TOKEN=ваш_токен_бота
   CHAT_ID=ваш_chat_id_из_@userinfobot
   ```

5. Запустите скрипт:

   ```bash
   python main.py
   ```

## Состав проекта

* `main.py` — основной скрипт бота
* `.env` — для секретов (не публикуется)
* `requirements.txt` — список зависимостей
* `.gitignore` — файлы/папки, исключенные из Git

## Важно

Никогда не заливайте `.env` в GitHub — это конфиденциальные данные!
