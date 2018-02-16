#!/usr/bin/env python
from __future__ import print_function

__author__ = "Mislav Novakovic <mislav.novakovic@sartura.hr>"
__copyright__ = "Copyright 2018, Deutsche Telekom AG"
__license__ = "BSD 3-Clause"

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import yang as ly
import unittest
import sys

import config

class TestUM(unittest.TestCase):
    def test_ly_ctx_new(self):
        print(config.TESTS_DIR)
        yang_folder1 = config.TESTS_DIR + "/data/files"
        yang_folder2 = config.TESTS_DIR + "/data:" + config.TESTS_DIR + "/data/files"
        try:
            ctx = ly.Context(yang_folder1)
            self.assertIsNotNone(ctx)
            list = ctx.get_searchdirs()
            self.assertIsNotNone(list)
            self.assertEqual(1, len(list))

            ctx = ly.Context(yang_folder2)
            self.assertIsNotNone(ctx)
            list = ctx.get_searchdirs()
            self.assertIsNotNone(list)
            self.assertEqual(2, len(list))

        except Exception as e:
            print(e)
            sys.exit()

    def test_ly_ctx_new_invalid(self):
        print(config.TESTS_DIR)
        yang_folder = "INVALID_PATH"
        try:
            ctx = ly.Context(yang_folder)
            self.fail("exception not thrown")

        except Exception as e:
            return

if __name__ == '__main__':
    unittest.main()