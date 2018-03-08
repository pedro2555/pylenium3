#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pylenium3

Copyright (C) 2018  Pedro Rodrigues <prodrigues1990@gmai.com>

This file is part of Pylenium3.

Pylenium3 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

Pylenium3 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Pylenium3.  If not, see <http://www.gnu.org/licenses/>.
"""
from setuptools import setup, find_packages

requirements = ['selenium']

setup_requirements = []

test_requirements = ['setuptools', 'mock', 'setuptools-lint', 'flake8']

setup(
    author="Pedro Rodrigues",
    author_email='prodrigues1990@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Pythonic wrapper for selenium",
    install_requires=requirements,
    license="GNU General Public License v2",
    include_package_data=True,
    keywords='selenium pylenium pylenium3',
    name='pylenium3',
    packages=find_packages(include=['pylenium3']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pedro2555/pylenium3',
    version='0.0.1',
    zip_safe=False,
)
