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
from tests import CHROMEDRIVER_PATH


class TestChrome(unittest.TestCase):

    def test_launch_headless(self):
        options = {
            'driver': CHROMEDRIVER_PATH,
            'headless': True
        }
        with Chrome(options=options) as d:
            d.get('https://www.google.com/')
