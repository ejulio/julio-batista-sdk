from http_client import DefaultHttpClient, UnauthorizedError
import json
from test_client import make_api_response
from test_movie import LOTR_1_FAKE_RESPONSE
import pytest

def test_get(requests_mock):
    response = make_api_response(LOTR_1_FAKE_RESPONSE)
    requests_mock.get("https://the-one-api.dev/v2/movie/123", text=json.dumps(response))
    http = DefaultHttpClient("apikey-123")

    result = http.get("movie/123")

    assert result == response
    assert requests_mock.last_request.headers["Authorization"] == "Bearer apikey-123"

def test_invalid_apikey():
    with pytest.raises(ValueError):
        DefaultHttpClient("")

def test_handle_401(requests_mock):
    requests_mock.get("https://the-one-api.dev/v2/movie/123", status_code=401, text="response 401")
    http = DefaultHttpClient("bad-api-key")

    with pytest.raises(UnauthorizedError) as e:
        http.get("movie/123")

        assert e.apikey == "bad-a..."
        assert e.response_text == "response 401"