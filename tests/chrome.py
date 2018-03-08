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
import unittest
from mock import patch

from pylenium3.chrome import Chrome
import selenium


@patch('selenium.webdriver.Chrome')
class TestChrome(unittest.TestCase):

    def test__init__(self, chrome):
        chrm = Chrome()
        self.assertIsNotNone(chrm._options)

    def test__init__withoptions(self, chrome):
        chrm = Chrome(options={})
        self.assertEqual(chrm.options, {})
        self.assertIsNotNone(chrm._options)

    def test_withcontext_enter(self, chrome):
        with Chrome() as chrm:
            self.assertIsNone(chrm.driver)

    def test_withcontext_cleansafterget(self, chrome):
        with Chrome() as chrome_context:
            chrome_context.get('')

        chrome.return_value.stop_client.assert_called_once()
        chrome.return_value.close.assert_called_once()
        chrome.return_value.quit.assert_called_once()

    def test___getitem__stringcallbyid(self, chrome):
        with Chrome() as chrome_context:
            chrome_context.get('')
            chrome_context['test']
            chrome.return_value.find_element_by_id.\
                assert_called_once_with('test')

    def test___getitem__idselectorcallbyid(self, chrome):
        with Chrome() as chrome_context:
            chrome_context.get('')
            chrome_context['id':'test']
            chrome.return_value.find_element_by_id.\
                assert_called_once_with('test')

    def test___getitem__nameselectorusesbyname(self, chrome):
        with Chrome() as chrome_context:
            chrome_context.get('')
            chrome_context['name':'test']
            chrome.return_value.find_elements_by_name.\
                assert_called_once_with('test')

    def test___getitem__xpathselectorusesbyxpath(self, chrome):
        with Chrome() as chrome_context:
            chrome_context.get('')
            chrome_context['xpath':'test']
            chrome.return_value.find_elements_by_xpath.\
                assert_called_once_with('test')

    def test___getitem__linkselectorusesbylink(self, chrome):
        with Chrome() as chrome_context:
            chrome_context.get('')
            chrome_context['link':'test']
            chrome.return_value.find_elements_by_link_text.\
                assert_called_once_with('test')

    def test___getitem__partiallinkselectorusesbypartiallink(self, chrome):
        with Chrome() as chrome_context:
            chrome_context.get('')
            chrome_context['partiallink':'test']
            chrome.return_value.find_elements_by_partial_link_text.\
                assert_called_once_with('test')

    def test___getitem__tagselectorusesbytag(self, chrome):
        with Chrome() as chrome_context:
            chrome_context.get('')
            chrome_context['tag':'test']
            chrome.return_value.find_elements_by_tag_name.\
                assert_called_once_with('test')

    def test___getitem__classselectorusesbyclass(self, chrome):
        with Chrome() as chrome_context:
            chrome_context.get('')
            chrome_context['class':'test']
            chrome.return_value.find_elements_by_class_name.\
                assert_called_once_with('test')

    def test___getitem__cssselectorusesbycss(self, chrome):
        with Chrome() as chrome_context:
            chrome_context.get('')
            chrome_context['css':'test']
            chrome.return_value.find_elements_by_css_selector.\
                assert_called_once_with('test')

    def test__getitem__raiseslookuperror(self, chrome):
        with Chrome() as chrome_context:
            chrome_context.get('')
            with self.assertRaises(LookupError) as _:
                chrome_context['invalid':'']
