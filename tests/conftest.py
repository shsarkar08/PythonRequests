import pytest

from uuid import uuid4
from utils.fileReader import read_file


@pytest.fixture
def create_data():
    payload = read_file('create_pet.json')
    pet_name = f'Doggie_file_{str(uuid4())}'
    payload['name'] = pet_name

    yield payload
