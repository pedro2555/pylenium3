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
        if self.driver is not None:
            self.driver.stop_client()
            self.driver.close()
            self.driver.quit()

    def get(self, url):
        self._lazyloadchrome()

        self.driver.get(url)

    def __getitem__(self, selector):

        if type(selector) is str:
            # assume it's an id
            query = selector
            selector = 'id'

        if type(selector) is slice:
            query = selector.stop
            selector = selector.start

        self._lazyloadchrome()

        if selector == 'id':
            return self.driver.find_element_by_id(query)
        elif selector == 'name':
            return self.driver.find_elements_by_name(query)
        elif selector == 'xpath':
            return self.driver.find_elements_by_xpath(query)
        elif selector == 'link':
            return self.driver.find_elements_by_link_text(query)
        elif selector == 'partiallink':
            return self.driver.find_elements_by_partial_link_text(query)
        elif selector == 'tag':
            return self.driver.find_elements_by_tag_name(query)
        elif selector == 'class':
            return self.driver.find_elements_by_class_name(query)
        elif selector == 'css':
            return self.driver.find_elements_by_css_selector(query)

        raise LookupError('Unknown selenium selector %s' % selector)
