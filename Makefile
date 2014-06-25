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
	pip uninstall Reddit-Image-Scrapper


clean:
	rm -rf reddit_scrapper/*.pyc
	rm -rf __pycache__
	rm -rf reddit_scrapper/__pycache__
	rm -rf build
	rm -rf *egg-info
	rm -rf dist
