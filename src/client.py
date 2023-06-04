from typing import Union, Iterable, Callable
from movie import Movie
from quote import Quote
from http_client import RequestsHttpClient, HttpClient


class Client:
    _http_client: HttpClient

    def __init__(self, apikey_or_client: Union[str, HttpClient]):
        if isinstance(apikey_or_client, str):
            apikey_or_client = RequestsHttpClient(apikey_or_client)

        self._http_client = apikey_or_client 

    def get_movie(self, movie_id: str) -> Movie:
        res = self._get_api_resource(f"movie/{movie_id}", Movie.from_api_response)
        if not res:
            return None
        return res[0]
    
    def get_movies(self) -> Iterable[Movie]:
        return self._get_api_resource("movie", Movie.from_api_response)

    def get_movie_quotes(self, movie_id) -> Iterable[Quote]:
        return self._get_api_resource(f"movie/{movie_id}/quote", Quote.from_api_response)
        
    def get_quotes(self) -> Iterable[Quote]:
        return self._get_api_resource("quote", Quote.from_api_response)
        
    def get_quote(self, quote_id: str) -> Quote:
        res = self._get_api_resource(f"quote/{quote_id}", Quote.from_api_response)
        if not res:
            return None
        return res[0]
    
    def _get_api_resource(self, url: str, parse: Callable) -> Iterable:
        docs = self._http_client.get(url)["docs"]
        return list(map(parse, docs))