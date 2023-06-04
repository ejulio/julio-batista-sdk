from typing import Protocol, Union, Iterable


class HttpClient(Protocol):
    def get(self, url: str) -> Union[dict, Iterable[dict]]:
        """Performs a HTTP GET request and returns the parsed result"""


class DefaultHttpClient:    
    def get(self, url: str) -> Union[dict, Iterable[dict]]:
        raise NotImplementedError()


class Client:
    _http_client: HttpClient

    def __init__(self, apikey_or_client: Union[str, HttpClient]):
        if isinstance(apikey_or_client, str):
            apikey_or_client = DefaultHttpClient(apikey_or_client)

        self._http_client = apikey_or_client 

