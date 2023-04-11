from json import dumps
import random
from uuid import uuid4

import requests
from utils.readProperties import ReadConfig

baseURI = ReadConfig.getBaseURI()


def create_new_pet_operation(base_uri):
    animal_name = f'Pet {str(uuid4())}'
    rand_id = random.randrange(99, 9999)
    payload = dumps({
        "id": rand_id,
        "name": f"Doggie_{animal_name}",
        "photoUrls": [
            "http://photourl.com"
        ],
        "status": "available"
    })
    headers = {
         'Content-type': 'application/json',
         'Accept': 'application/json'
    }

    res = requests.post(f'{base_uri}/pet', data=payload, headers=headers)
    return res


class TestPetStoreAPIs:

    def test_create_new_pet(self):

        resp = create_new_pet_operation(baseURI)
        print(resp.url)
        print(f'Op Status: {resp.status_code}')
        json_resp = resp.json()
        print(f"Id: {json_resp.get('id')}, Name: {json_resp.get('name')}")
