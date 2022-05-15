import requests
import os
import argparse
from dotenv import load_dotenv
from urllib.parse import urlsplit


def create_bitlink(token, short_url):
    full_url = f'http://{short_url}'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    user_info = requests.get('https://api-ssl.bitly.com/v4/user', headers=headers)
    group_guid = user_info.json()['default_group_guid']

    data = {
        "group_guid": group_guid,
        "long_url": full_url
    }

    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', json=data, headers=headers)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(token, short_url):

    headers = {
        'Authorization': f'Bearer {token}',
    }

    params = (
        ('unit', 'day'),
        ('units', '-1'),
    )

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{short_url}/clicks/summary', headers=headers, params=params)
    return response.json()["total_clicks"]


def check_bitlink(token, short_url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{short_url}', headers=headers)
    return response.ok


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description='Введите ссылку: ')
    parser.add_argument('url', help='Ссылка которую вы хотели бы сократить')
    args = parser.parse_args()

    token = os.getenv("BITLY_TOKEN")
    user_url = args.url
    short_url = ''.join(urlsplit(user_url)[1:])

    if check_bitlink(token, short_url):
        try:
            total_clicks = count_clicks(token, short_url)
            print(total_clicks)
        except requests.exceptions.HTTPError:
            print('Не удалось получить информацию о количестве переходов по ссылке')
    else:
        try:
            bitlink = making_bitlink(token, short_url)
            print(bitlink)
        except requests.exceptions.HTTPError:
            print('Не удалось создать ссылку, т.к. что-то пошло не так')