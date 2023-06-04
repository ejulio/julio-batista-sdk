from typing import Union, Iterable
from movie import Movie
from quote import Quote
from http_client import DefaultHttpClient, HttpClient

class Client:
    _http_client: HttpClient

    def __init__(self, apikey_or_client: Union[str, HttpClient]):
        if isinstance(apikey_or_client, str):
            apikey_or_client = DefaultHttpClient(apikey_or_client)

        self._http_client = apikey_or_client 

    def get_movie(self, movie_id: str) -> Movie:
        docs = self._http_client.get(f"movie/{movie_id}")["docs"]
        if not docs:
            return None
        return Movie.from_api_response(docs[0])
    
    def get_movies(self) -> Iterable[Movie]:
        docs = self._http_client.get("movie")["docs"]
        return list(map(Movie.from_api_response, docs))

    def get_movie_quotes(self, movie_id) -> Iterable[Quote]:
        docs = self._http_client.get(f"movie/{movie_id}/quote")["docs"]
        return list(map(Quote.from_api_response, docs))
    
    def get_quotes(self) -> Iterable[Quote]:
        docs = self._http_client.get("quote")["docs"]
        return list(map(Quote.from_api_response, docs))

    def get_quote(self, quote_id: str) -> Quote:
        docs = self._http_client.get(f"quote/{quote_id}")["docs"]
        if not docs:
            return None
        return Quote.from_api_response(docs[0])
    
