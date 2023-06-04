from movie import Movie

def test_from_api_response():
    m = Movie.from_api_response({
        "_id": "123",
        "name": "LOTR",
        "runtimeInMinutes": 60,
        "budgetInMillions": 100,
        "boxOfficeRevenueInMillions": 135,
        "academyAwardNominations": 5,
        "academyAwardWins": 4,
        "rottenTomatoesScore": 99
    })

    assert m.ID == "123"
    assert m.name == "LOTR"
    assert m.runtime_in_minutes == 60
    assert m.budget_in_millions == 100
    assert m.box_office_revenue_in_millions == 135
    assert m.academy_award_nominations == 5
    assert m.academy_award_wins == 4
    assert m.rotten_tomatoes_score == 99
