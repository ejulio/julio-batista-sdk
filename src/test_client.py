from client import Client
from movie import Movie

LOTR_1_FAKE_RESPONSE = {
    "_id":"123",
    "name":"LOTR",
    "runtimeInMinutes":1,
    "budgetInMillions":2,
    "boxOfficeRevenueInMillions":3,
    "academyAwardNominations":4,
    "academyAwardWins":5,
    "rottenTomatoesScore":6
}

LOTR_2_FAKE_RESPONSE = {
    "_id":"456",
    "name":"LOTR 2",
    "runtimeInMinutes":6,
    "budgetInMillions":5,
    "boxOfficeRevenueInMillions":4,
    "academyAwardNominations":3,
    "academyAwardWins":2,
    "rottenTomatoesScore":1
}


class FakeHttpClient:

    _responses: dict

    def __init__(self):
        self._responses = {
            "movie/123": {
                "docs":[LOTR_1_FAKE_RESPONSE],
                "total":1,
                "limit":1000,
                "offset":0,
                "page":1,
                "pages":1
            },
            "movie": {
                "docs":[LOTR_1_FAKE_RESPONSE, LOTR_2_FAKE_RESPONSE],
                "total":1,
                "limit":1000,
                "offset":0,
                "page":1,
                "pages":1
            },
            "movie/missing": {
                "docs":[],
                "total":1,
                "limit":1000,
                "offset":0,
                "page":1,
                "pages":1
            }
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