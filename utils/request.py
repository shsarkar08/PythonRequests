from dataclasses import dataclass

import requests


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict
    url: str


class APIRequest:
    def get(self, url, params=None):
        if params is None:
            response = requests.get(url)
            return self.__api_response(response)
        else:
            response = requests.get(url, params=params)
            return self.__api_response(response)

    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        return self.__api_response(response)

    def put(self, url, payload, headers):
        response = requests.put(url, data=payload, headers=headers)
        return self.__api_response(response)

    def delete(self, url):
        response = requests.delete(url)
        return self.__api_response(response)

    def __api_response(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers
        url = response.url

        return Response(status_code, text, as_dict, headers, url)
