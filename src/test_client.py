
from typing import Union, Iterable
from client import Client
from movie import Movie
from quote import Quote
from test_movie import LOTR_1_FAKE_RESPONSE, LOTR_2_FAKE_RESPONSE
from test_quote import QUOTE_1_FAKE_RESPONSE, QUOTE_2_FAKE_RESPONSE


def make_api_response(docs: Union[dict, Iterable[dict]]) -> dict:
    if isinstance(docs, dict):
        docs = [docs]

    return {
        "docs": docs,
        "total": 1,
        "limit": 1000,
        "offset": 0,
        "page": 1,
        "pages": 1
    }


class FakeHttpClient:

    _responses: dict

    def __init__(self):
        self._responses = {
            "movie/123": make_api_response(LOTR_1_FAKE_RESPONSE),
            "movie": make_api_response([LOTR_1_FAKE_RESPONSE, LOTR_2_FAKE_RESPONSE]),
            "movie/missing": make_api_response([]),
            "quote/123": make_api_response(QUOTE_1_FAKE_RESPONSE),
            "quote/missing": make_api_response([]),
            "quote": make_api_response([QUOTE_1_FAKE_RESPONSE, QUOTE_2_FAKE_RESPONSE]),
            "movie/456/quote": make_api_response([QUOTE_1_FAKE_RESPONSE]),
            "movie/123/quote": make_api_response([]),
        }

    def get(self, url) -> dict:
        return self._responses[url]


def test_get_movie():
    c = Client(FakeHttpClient())
    movie = c.get_movie("123")

    assert movie == Movie.from_api_response(LOTR_1_FAKE_RESPONSE)

def test_get_missing_movie():
    c = Client(FakeHttpClient())
    movie = c.get_movie("missing")

    assert movie is None


def test_get_movies():
    c = Client(FakeHttpClient())
    movies = c.get_movies()

    assert len(movies) == 2
    assert movies[0] == Movie.from_api_response(LOTR_1_FAKE_RESPONSE)
    assert movies[1] == Movie.from_api_response(LOTR_2_FAKE_RESPONSE)

def test_get_quote():
    c = Client(FakeHttpClient())
    quote = c.get_quote("123")

    assert quote == Quote.parse_api_response(QUOTE_1_FAKE_RESPONSE)

def test_get_missing_quote():
    c = Client(FakeHttpClient())
    quote = c.get_quote("missing")

    assert quote is None

def test_get_quotes():
    c = Client(FakeHttpClient())
    quotes = c.get_quotes()

    assert len(quotes) == 2
    assert quotes[0] == Quote.parse_api_response(QUOTE_1_FAKE_RESPONSE)
    assert quotes[1] == Quote.parse_api_response(QUOTE_2_FAKE_RESPONSE)

def test_get_movie_quotes():
    c = Client(FakeHttpClient())
    quotes = c.get_movie_quotes("456")

    assert len(quotes) == 1
    assert quotes[0] == Quote.parse_api_response(QUOTE_1_FAKE_RESPONSE)

def test_get_missing_movie_quotes():
    c = Client(FakeHttpClient())
    quotes = c.get_movie_quotes("123")

    assert len(quotes) == 0