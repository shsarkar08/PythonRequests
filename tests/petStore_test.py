from json import dumps
import random
from uuid import uuid4

import requests
from utils.readProperties import ReadConfig

baseURI = ReadConfig.getBaseURI()


def get_pet_by_id_operation(base_uri, pet_id):
    res = requests.get(f'{base_uri}/pet/{pet_id}')
    return res


def get_pet_by_status_operation(base_uri, status):
    params = {
        'status': status
    }
    res = requests.get(f'{base_uri}/pet/findByStatus', params=params)
    return res


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
        'Content-Type': 'application/json'
    }

    res = requests.post(f'{base_uri}/pet', data=payload, headers=headers)
    return res


class TestPetStoreAPIs:
    def test_get_by_pet_id(self):
        resp = get_pet_by_id_operation(baseURI, 15)
        json_resp = resp.json()
        print(resp.url)
        print(f'Op Status: {resp.status_code}')
        if resp.status_code == 200:
            print(f"ID: {json_resp['id']}, Name: {json_resp['name']}")

    def test_get_by_status(self):
        resp = get_pet_by_status_operation(baseURI, 'available')
        json_resp = resp.json()
        print(resp.url)
        print(f'Op Status: {resp.status_code}')
        print(f'Total records: {len(json_resp)}')

    def test_create_new_pet(self):

        resp = create_new_pet_operation(baseURI)
        print(resp.url)
        print(f'Op Status: {resp.status_code}')
        json_resp = resp.json()
        print(f"Id: {json_resp.get('id')}, Name: {json_resp.get('name')}")
