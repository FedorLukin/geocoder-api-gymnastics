import sys
import requests
from PIL import Image
from io import BytesIO
from get_objects import get_objects_data


toponym_to_find = " ".join(sys.argv[1:])
spn, objects = get_objects_data(toponym_to_find)

apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

map_params = {
    "ll": objects[0].point,
    "spn": spn,
    "apikey": apikey,
    "pt": f'{objects[0].point},round'
}

map_api_server = "https://static-maps.yandex.ru/v1"
response = requests.get(map_api_server, params=map_params)
im = BytesIO(response.content)
opened_image = Image.open(im)
opened_image.show()
