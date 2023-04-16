class BaseClient:
    def __init__(self):
        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
