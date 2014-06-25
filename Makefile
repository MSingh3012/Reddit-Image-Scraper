init:
	pip install -r requirements.txt

test:
	nosetests

.PHONY: clean

build:
	python setup.py build

dist:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

uninstall:
	pip uninstall Reddit-Image-Scraper


clean:
	rm -rf reddit_scraper/*.pyc
	rm -rf __pycache__
	rm -rf reddit_scraper/__pycache__
	rm -rf build
	rm -rf *egg-info
	rm -rf dist
