from app.reasoning import reason

def test_empty_context():
    assert reason("", "test") == "I don't know"
