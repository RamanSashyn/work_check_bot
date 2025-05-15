import os
import time
import requests
from dotenv import load_dotenv
from telegram import Bot


def send_notification(bot, chat_id, message):
    bot.send_message(chat_id=chat_id, text=message)


def main():
    load_dotenv()

    dvmn_token = os.environ['DVMN_TOKEN']
    bot_token = os.environ['BOT_TOKEN']
    tg_chat_id = int(os.environ['TG_CHAT_ID'])

    bot = Bot(token=bot_token)

    headers = {
        'Authorization': f'Token {dvmn_token}',
    }

    params = {}
    while True:
        try:
            response = requests.get('https://dvmn.org/api/long_polling/', params=params, headers=headers, timeout=90)
            response.raise_for_status()
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
                    send_notification(bot, tg_chat_id, message)

        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            time.sleep(60)
            continue
        except requests.exceptions.JSONDecodeError:
            continue


if __name__ == '__main__':
    main()
