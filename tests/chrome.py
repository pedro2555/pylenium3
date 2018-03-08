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
from mock import Mock, MagicMock, patch
from contextlib import suppress

from pylenium3.chrome import Chrome
import selenium

@patch('selenium.webdriver.Chrome')
class TestChrome(unittest.TestCase):

    def test__init__withoutoptions_initschrome(self, chrome):
        Chrome()
        chrome.assert_called_once()

    @patch('selenium.webdriver.chrome.options.Options')
    def test__init__withoptions_initsoptions(self, chrome, options):
        Chrome(options={})
        options.assert_called_once()

    def test_withcontext_cleanschrome(self, chrome):
        with Chrome() as c:
            pass

        chrome.return_value.stop_client.assert_called_once()
        chrome.return_value.close.assert_called_once()
        chrome.return_value.quit.assert_called_once()
