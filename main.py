import os
import requests
import asyncio
from dotenv import load_dotenv
from aiogram import Bot


def send_notification(bot, message, chat_id):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.send_message(chat_id, message))


def main():
    load_dotenv()

    dvmn_token = os.getenv('DVMN_TOKEN')
    bot_token = os.getenv('BOT_TOKEN')
    tg_chat_id = int(os.getenv('TG_CHAT_ID'))

    bot = Bot(token=bot_token)

    headers = {
        'Authorization': f'Token {dvmn_token}',
    }

    params = {}
    while True:
        try:
            response = requests.get('https://dvmn.org/api/long_polling/', params=params, headers=headers, timeout=90)
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
                    send_notification(bot, message, tg_chat_id)

        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            continue
        except requests.exceptions.JSONDecodeError:
            continue


if __name__ == '__main__':
    main()
