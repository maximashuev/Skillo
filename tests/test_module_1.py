from app import rev_str


def test_one():
    assert rev_str("der", ["d"]) == "Re"
