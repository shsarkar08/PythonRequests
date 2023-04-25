from json import dumps
import requests
from utils.readProperties import ReadConfig

baseURI = ReadConfig.getBaseURI()


class PtClient:

    def create_new_pet_operation(self, body):
        payload = dumps(body)
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }

        res = requests.post(f'{baseURI}/pet', data=payload, headers=headers)
        return res


client = PtClient()


def test_create_new_pet(create_data):
    resp = client.create_new_pet_operation(create_data)
    print(resp.url)
    print(f'Op Status: {resp.status_code}')
    json_resp = resp.json()
    print(json_resp)
    print(f"Id: {json_resp.get('id')}, Name: {json_resp.get('name')}")
