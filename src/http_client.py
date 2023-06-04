from typing import Protocol
import requests
from os import path


class HttpClient(Protocol):
    def get(self, url: str) -> dict:
        """Performs a HTTP GET request and returns the parsed result"""


class DefaultHttpClient:    
    _apikey: str
    _base_url: str = "https://the-one-api.dev/v2/"

    def __init__(self, apikey: str):
        self._apikey = apikey

    def get(self, url: str) -> dict:
        return requests.get(path.join(self._base_url, url), headers={
            "Authorization": f"Bearer {self._apikey}"
        }).json()