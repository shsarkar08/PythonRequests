import random
from json import dumps
from uuid import uuid4

from utils.request import APIRequest
from clients.base_client import BaseClient
from utils.readProperties import ReadConfig


class PetClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = ReadConfig.getBaseURI()
        self.request = APIRequest()

    def read_pet_by_id(self, pet_id):
        url = f'{self.base_url}/pet/{pet_id}'
        return self.request.get(url)

    def read_pet_by_status(self, pet_status):
        url = f'{self.base_url}/pet/findByStatus'
        params = {
            'status': pet_status
        }
        return self.request.get(url, params)

    def create_new_pet(self, body=None):
        response = self.__create_pet_with_unique_name_id(body)
        return response

    def __create_pet_with_unique_name_id(self, body=None):
        url = f'{self.base_url}/pet'
        if body is None:
            pet_id = random.randrange(99, 9999)
            pet_name = f'Doggie_{str(uuid4())}'
            payload = dumps(
                {
                    "id": pet_id,
                    "name": pet_name,
                    "status": "available"
                }
            )
        else:
            payload = dumps(body)
        return self.request.post(url, payload, self.headers)

    def delete_pet(self, pet_id):
        url = f'{self.base_url}/pet/{pet_id}'
        return self.request.delete(url)
