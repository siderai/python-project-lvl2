lint:
	poetry run flake8 gendiff

diff:
	python gendiff/gendiff.py

test:
	poetry run pytest
