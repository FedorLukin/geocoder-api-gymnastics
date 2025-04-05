import requests
from dataclasses import dataclass


@dataclass
class Object:
    point: tuple
    spn: tuple


def get_object_size_and_cords(object_name):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

    search_params = {
        "apikey": api_key,
        "text": object_name,
        "lang": "ru_RU",
        "type": "biz"
    }

    json_response = requests.get(search_api_server, params=search_params).json()
    geoobject_data = json_response['features'][0]
    cords = ','.join(map(str, geoobject_data['geometry']['coordinates']))
    ln1, lt1 = geoobject_data['properties']['boundedBy'][0]
    ln2, lt2 = geoobject_data['properties']['boundedBy'][1]
    spn = f'{round(abs(ln1 - ln2), 4)},{round(abs(lt1 - lt2), 4)}'

    return Object(point=cords, spn=spn)
