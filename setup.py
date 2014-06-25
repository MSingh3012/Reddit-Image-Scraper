# -*- coding: utf-8 -*-
import reddit_scraper

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Reddit-Image-Scraper',
    description='Web scraper for reddit images',
    author='Rookev',
    url='https://github.com/Rookev/Reddit-Image-Scraper.git',
    include_package_data=True,
    test_require=['nose'],
    version=reddit_scraper.__version__,
    packages=['reddit_scraper'],
    entry_points={
        'console_scripts':
            [
                'reddit_scraper = reddit_scraper.__main__:main',
            ]
        }
)
