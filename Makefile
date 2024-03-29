coverage:
	pytest --cov=storage --cov-report html

build:
	python3 -m build && \
	pip install twine --upgrade && \
	twine upload dist/*
