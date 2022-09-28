black:
	@black ./market_data --check

flake8:
	@flake8 ./market_data --max-line-length 79

isort:
	@isort ./market_data

checks:
	@make black
	@make flake8