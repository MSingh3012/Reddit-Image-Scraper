# -*- coding: utf-8 -*-
import reddit_scrapper

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Reddit-Image-Scrapper',
    description='Web scrapper for reddit images',
    author='Rookev',
    url='https://github.com/Rookev/Reddit-Image-Scraper.git',
    include_package_data=True,
    test_require=['nose'],
    version=reddit_scrapper.__version__,
    packages=['reddit_scrapper'],
    entry_points={
        'console_scripts':
            [
                'reddit_scrapper = reddit_scrapper.__main__:main',
            ]
        }
)
