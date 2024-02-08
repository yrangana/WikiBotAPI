install:
		pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
		python -m pytest -vv tests/*.py

format:
		black *.py scrapebot/*.py tests/*.py

lint:
		pylint --disable=R,C *.py scrapebot/*.py tests/*.py

all: install format lint test
