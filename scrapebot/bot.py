import wikipedia


def get_wikipedia_summary(query, length):
    try:
        return wikipedia.summary(query, sentences=length)
    except wikipedia.exceptions.DisambiguationError as e:
        query = e.options[0]
        return wikipedia.summary(query, sentences=length)
    except wikipedia.exceptions.PageError:
        return "No results found for the given keywords."
