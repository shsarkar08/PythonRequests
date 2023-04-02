import requests
from utils.readProperties import ReadConfig

baseURI = ReadConfig.getBaseURI()


def get_pet_by_id_operation(base_url, pet_id):
    res = requests.get(f'{base_url}/pet/{pet_id}')
    return res


class TestPetStoreAPIs:
    def test_get_op(self):
        resp = get_pet_by_id_operation(baseURI, 15)
        json_resp = resp.json()
        print(resp.url)
        print(f'Op Status: {resp.status_code}')
        print(f"ID: {json_resp['id']}, Name: {json_resp['name']}")

