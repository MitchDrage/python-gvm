# -*- coding: utf-8 -*-
# Copyright (C) 2021-2022 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from gvm.errors import InvalidArgument
from gvm.protocols.gmpv214 import HostsOrdering


class GetHostsOrderingFromStringTestCase(unittest.TestCase):
    def test_invalid(self):
        with self.assertRaises(InvalidArgument):
            HostsOrdering.from_string("foo")

    def test_none_or_empty(self):
        ct = HostsOrdering.from_string(None)
        self.assertIsNone(ct)
        ct = HostsOrdering.from_string("")
        self.assertIsNone(ct)

    def test_sequential(self):
        ct = HostsOrdering.from_string("sequential")
        self.assertEqual(ct, HostsOrdering.SEQUENTIAL)

    def test_random(self):
        ct = HostsOrdering.from_string("random")
        self.assertEqual(ct, HostsOrdering.RANDOM)

    def test_reverse(self):
        ct = HostsOrdering.from_string("reverse")
        self.assertEqual(ct, HostsOrdering.REVERSE)
