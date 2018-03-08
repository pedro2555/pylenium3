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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException


class Chrome(object):

    def __init__(self, **kwargs):
        self.driver = None
        self.options = kwargs['options'] if 'options' in kwargs else None
        self._options = Options()

    def _lazyloadchrome(self):
        if self.driver is None:
            try:
                self.driver = webdriver.Chrome(options=self._options)
            except WebDriverException as crap:
                raise FileNotFoundError(str(crap))

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._lazyloadchrome()

        self.driver.stop_client()
        self.driver.close()
        self.driver.quit()

    def get(self, url):
        self._lazyloadchrome()

        self.driver.get(url)

    def __getitem__(self, id):
        self._lazyloadchrome()

        return self.driver.find_element_by_id(id)
