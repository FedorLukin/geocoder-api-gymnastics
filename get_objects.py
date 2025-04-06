import requests
from dataclasses import dataclass
from typing import Union, List


@dataclass
class Object:
    workschedule: Union[None, bool]
    point: tuple


def get_objects_data(object_name: str, address_ll: str = None, limit: int = 1) -> List[Object]:
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

    search_params = {
        "apikey": api_key,
        "text": object_name,
        "lang": "ru_RU",
        'll': address_ll,
        "type": "biz"
    }

    json_response = requests.get(search_api_server, params=search_params).json()
    results = []

    for geoobject_data in json_response['features']:
        company_data = geoobject_data['properties'].get('CompanyMetaData')
        if not company_data:
            continue
        schedule = 3 if not company_data['Hours'] else \
            int(company_data['Hours']['Availabilities'][0].get('TwentyFourHours', 0))
        cords = ','.join(map(str, geoobject_data['geometry']['coordinates']))
        results.append(Object(workschedule=schedule, point=cords))
        if len(results) == limit:
            break

    if limit == 1:
        ln1, lt1 = json_response['features'][0]['properties']['boundedBy'][0]
        ln2, lt2 = json_response['features'][0]['properties']['boundedBy'][1]
        spn = f'{round(abs(ln1 - ln2), 4)},{round(abs(lt1 - lt2), 4)}'

    else:
        point_ln, point_lt = map(float, address_ll.split(','))
        max_ln = max(map(lambda x: float(x.point.split(',')[0]), results))
        min_ln = min(map(lambda x: float(x.point.split(',')[0]), results))
        max_lt = max(map(lambda x: float(x.point.split(',')[1]), results))
        min_lt = min(map(lambda x: float(x.point.split(',')[1]), results))
        dt_ln = max(abs(max_ln - point_ln), abs(point_ln - min_ln))
        dt_lt = max(abs(max_lt - point_lt), abs(point_lt - min_lt))
        print(dt_ln, dt_lt)
        spn = f'{round(dt_ln, 5) * 2},{round(dt_lt, 5) * 2}'

    return (spn, results)
