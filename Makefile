black:
	@black ./market_data --check

flake8:
	@flake8 ./market_data --max-line-length 79 --exclude=tests

isort:
	@isort ./market_data --check --skip="./market_data/tests/*"

reqs:
	@pip install -r requirements.txt

tests:
	@( cd market_data && python -m pytest --cov-config=../.coveragerc --cov-report term-missing --cov . -ra ./tests)
	@( cd market_data && python -m pytest  -ra ./tests)

checks:
	@make reqs
	@make black
	@make flake8
	@make isort
	