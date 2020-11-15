#!/usr/bin/env python2

import setuptools

description = 'Error highlight plugin for Flake8.'

with open('README.md', 'r') as fobj:
    long_description = fobj.read()

requires = [
    "flake8 > 3.0.0",
]

setuptools.setup(
    name="flake8-colors",
    license="MIT",
    version="0.1.8",
    description=description,
    long_description=long_description or description,
    long_description_content_type='text/markdown',
    author="Andrew Dunai",
    author_email="andrew@dun.ai",
    url="https://github.com/and3rson/flake8-colors",
    packages=[
        "flake8_colors",
    ],
    install_requires=requires,
    entry_points={
        'flake8.extension': [
            'flake8-colors = flake8_colors:ColorFormatter',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
