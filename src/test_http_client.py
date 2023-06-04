from http_client import DefaultHttpClient
import json
from test_client import make_api_response
from test_movie import LOTR_1_FAKE_RESPONSE


def test_get(requests_mock):
    response = make_api_response(LOTR_1_FAKE_RESPONSE)
    requests_mock.get("https://the-one-api.dev/v2/movie/123", text=json.dumps(response))
    http = DefaultHttpClient("apikey-123")

    result = http.get("movie/123")

    assert result == response
    assert requests_mock.last_request.headers["Authorization"] == "Bearer apikey-123"
