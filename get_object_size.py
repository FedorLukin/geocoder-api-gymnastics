import requests
from dataclasses import dataclass
import json


@dataclass
class Object:
    ln: float
    lt: float
    size: float


def get_object_size_and_cords(object_name):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

    search_params = {
        "apikey": api_key,
        "text": object_name,
        "lang": "ru_RU",
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)
    json_response = response.json()
    with open('zxc.json', 'w', encoding='UTF-8') as jsonfile:
        json.dump(json_response, jsonfile, ensure_ascii=False, indent=2)


get_object_size_and_cords('Красноярск, ФМШ СФУ')