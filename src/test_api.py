import os
import pytest
from client import Client


def test_api():
    """This is an end to end test to ensure the SDK
    hits the API and handles the responses properly"""
    apikey = os.environ.get("TEST_APIKEY")
    if apikey is None:
        pytest.skip("TEST_APIKEY not set, skipping...")
    
    client = Client(apikey)

    movies = client.get_movies()
    assert len(movies) > 0
    print("## MOVIES ##\n", movies)

    for movie in filter(lambda x: x.name == "The Two Towers", movies):
        print(movie)

        m = client.get_movie(movie.ID)
        print(m)

        quotes = client.get_movie_quotes(m.ID)
        print(f"## {len(quotes)} QUOTES ##\n", quotes)
    
    quotes = client.get_quotes()
    assert len(quotes) > 0
    print("## QUOTES ##\n", quotes)

    for quote in quotes[:3]:
        print(quote)

        q = client.get_quote(quote.ID)
        print(q)
