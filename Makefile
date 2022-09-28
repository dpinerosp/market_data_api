black:
	@black ./market_data --check

flake8:
	@flake8 ./market_data --max-line-length 79

isort:
	@isort ./market_data

pylint:
	@pylint ./market_data 

reqs:
	@pip install -r requirements.txt

checks:
	@make reqs
	@make black
	@make flake8