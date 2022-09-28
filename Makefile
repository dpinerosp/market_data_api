black:
	@black ./market_data --check

flake8:
	@flake8 ./market_data --max-line-length 79

checks:
	@make black
	@make flake8