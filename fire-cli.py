import fire
from scrapebot.bot import get_wikipedia_summary

if __name__ == "__main__":
    fire.Fire(get_wikipedia_summary)