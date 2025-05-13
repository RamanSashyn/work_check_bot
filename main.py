import os
import requests
import asyncio
from dotenv import load_dotenv
from aiogram import Bot


load_dotenv()

DVMN_TOKEN = os.getenv('DVMN_TOKEN')
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = int(os.getenv('CHAT_ID'))

bot = Bot(token=BOT_TOKEN)

devman_url = 'https://dvmn.org/api/long_polling/'
headers = {
    'Authorization': f'Token {DVMN_TOKEN}',
}

params = {}
while True:
    try:
        response = requests.get(devman_url, params=params, headers=headers, timeout=90)
        reviews_response = response.json()

        if reviews_response['status'] == 'timeout':
            params['timestamp'] = reviews_response['timestamp_to_request']

        elif reviews_response['status'] == 'found':
            params['timestamp'] = reviews_response['last_attempt_timestamp']

            for attempt in reviews_response['new_attempts']:
                lesson = attempt['lesson_title']
                lesson_url = attempt['lesson_url']
                if attempt['is_negative']:
                    message = (
                        f'У вас проверили работу "{lesson}"\n\n'
                        f'К сожалению, в работе нашлись ошибки.\n\n'
                        f'Ссылка на урок: {lesson_url}'
                    )
                else:
                    message = (
                        f'У вас проверили работу "{lesson}"\n\n'
                        f'Преподавателю все понравилось, можно приступать к следующему уроку!\n\n'
                        f'Ссылка на урок: {lesson_url}'
                    )

                loop = asyncio.get_event_loop()
                loop.run_until_complete(bot.send_message(CHAT_ID, message))

    except requests.exceptions.ReadTimeout as e:
        continue
    except requests.exceptions.ConnectionError as e:
        continue
    except requests.exceptions.JSONDecodeError as e:
        continue