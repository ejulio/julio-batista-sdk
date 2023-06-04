from quote import Quote

def test_parse_pai_response():
    q = Quote.parse_api_response({
        "_id": "123",
        "dialog": "this is a test",
        "movie": "456",
        "character": "789",
        "id": "123"
    })

    assert q.ID == "123"
    assert q.dialog == "this is a test"
    assert q.movie_id == "456"
    assert q.character_id == "789"