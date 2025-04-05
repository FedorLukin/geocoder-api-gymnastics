import sys
import requests
from PIL import Image
from io import BytesIO
from get_object import get_object_size_and_cords

toponym_to_find = " ".join(sys.argv[1:])
object = get_object_size_and_cords(toponym_to_find)

apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

map_params = {
    "ll": object.point,
    "spn": object.spn,
    "apikey": apikey,
    "pt": f'{object.point},round'
}

map_api_server = "https://static-maps.yandex.ru/v1"
response = requests.get(map_api_server, params=map_params)
im = BytesIO(response.content)
opened_image = Image.open(im)
opened_image.show()
