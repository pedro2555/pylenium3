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
            pass

    def test_withcontext_cleansafterget(self, chrome):
        with Chrome() as chrome_context:
            chrome_context.get('')
            pass

        chrome.return_value.stop_client.assert_called_once()
        chrome.return_value.close.assert_called_once()
        chrome.return_value.quit.assert_called_once()
