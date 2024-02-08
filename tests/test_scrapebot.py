from scrapebot.bot import get_wikipedia_summary


def test_get_wikipedia_summary():
    assert "Ceylon" in get_wikipedia_summary("Sri Lanka", 1)
    assert "Sri Lanka" in get_wikipedia_summary("Sri Lanka", 2)
    assert "No results found" in get_wikipedia_summary("Sri Lanka123", 2)
