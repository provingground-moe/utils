#
# LSST Data Management System
# Copyright 2008-2016 LSST Corporation.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
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
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.
#
from builtins import range

import sys
import math
import unittest

import lsst.utils.tests
import lsst.utils as lsstutils


class RaDecToStrTestCase(lsst.utils.tests.TestCase):
    """Convert angles to strings"""

    def setUp(self):
        self.goodData = [
            # Ra (deg)      Dec (deg)      Ra (str)       Dec (str)
            [0.00000000, 0.00000000,   "00:00:00.00", "+00:00:00.00"],
            [0.00027778, 0.00000000,   "00:00:00.07", "+00:00:00.00"],
            [0.00416667, 0.00000000,   "00:00:01.00", "+00:00:00.00"],
            [0.01666667, 0.00000000,   "00:00:04.00", "+00:00:00.00"],
            [1.00000000, 0.00000000,   "00:04:00.00", "+00:00:00.00"],
            [15.00000000, 0.00000000,  "01:00:00.00", "+00:00:00.00"],
            [0.00000000, 0.00027778,   "00:00:00.00", "+00:00:01.00"],
            [0.00000000, -0.00027778,  "00:00:00.00", "-00:00:01.00"],
            [0.00000000, 0.01666667,   "00:00:00.00", "+00:01:00.00"],
            [0.00000000, -0.01666667,  "00:00:00.00", "-00:01:00.00"],
            [0.00000000, 1.00000000,   "00:00:00.00", "+01:00:00.00"],
            [0.00000000, -1.00000000,  "00:00:00.00", "-01:00:00.00"],
            [0.00000000, 15.00000000,  "00:00:00.00", "+15:00:00.00"],
            [0.00000000, -15.00000000, "00:00:00.00", "-15:00:00.00"],
            [13.755500, 13.755500,     "00:55:01.32", "+13:45:19.79"],
            [213.755500, 0.000000000,  "14:15:01.32", "+00:00:00.00"],
            [80.15416667, +30.8077778, "05:20:37.00", "+30:48:28.00"],
            [80.15416667, -30.8077778, "05:20:37.00", "-30:48:28.00"],
            [15.,        15.,          "01:00:00.00", "+15:00:00.00"],
            [120,        -90,          "08:00:00.00", "-90:00:00.00"],
        ]

        self.raDegCol = 0
        self.decDegCol = 1
        self.raStrCol = 2
        self.decStrCol = 3
        self.num = len(self.goodData)

    # Testing numbers to strings

    def testRaRadToStr(self):
        for i in range(self.num):
            raDeg = self.goodData[i][self.raDegCol]
            raRad = raDeg*math.pi/180.
            raStr = self.goodData[i][self.raStrCol]
            self.assertEqual(lsstutils.raRadToStr(raRad), raStr)

    def testRaDegToStr(self):
        for i in range(self.num):
            raDeg = self.goodData[i][self.raDegCol]
            raStr = self.goodData[i][self.raStrCol]
            self.assertEqual(lsstutils.raDegToStr(raDeg), raStr)

    def testDecRadToStr(self):
        for i in range(self.num):
            decDeg = self.goodData[i][self.decDegCol]
            decRad = decDeg*math.pi/180.
            decStr = self.goodData[i][self.decStrCol]

            self.assertEqual(lsstutils.decRadToStr(decRad), decStr)

    def testDecDegToStr(self):
        for i in range(self.num):
            decDeg = self.goodData[i][self.decDegCol]
            decStr = self.goodData[i][self.decStrCol]
            self.assertEqual(lsstutils.decDegToStr(decDeg), decStr)

    def testRoundingDec(self):

        self.assertEqual(lsstutils.decDegToStr(15.0), "+15:00:00.00")
        self.assertEqual(lsstutils.decDegToStr(15.00000001), "+15:00:00.00")
        self.assertEqual(lsstutils.decDegToStr(15.00000001), "+15:00:00.00")

        self.assertEqual(lsstutils.decDegToStr(14.9999), "+14:59:59.64")
        self.assertEqual(lsstutils.decDegToStr(14.99999), "+14:59:59.96")
        self.assertEqual(lsstutils.decDegToStr(14.999999), "+14:59:59.99")
        self.assertEqual(lsstutils.decDegToStr(14.9999999), "+15:00:00.00")

    # Testing strings to numbers

    def testRaStrToRad(self):
        for i in range(self.num):
            raDeg = self.goodData[i][self.raDegCol]
            raRad = raDeg*math.pi/180.
            raStr = self.goodData[i][self.raStrCol]
            self.assertAlmostEqual(lsstutils.raStrToRad(raStr), raRad, 6)

    def testRaStrToDeg(self):
        for i in range(self.num):
            raDeg = self.goodData[i][self.raDegCol]
            raStr = self.goodData[i][self.raStrCol]
            self.assertAlmostEqual(lsstutils.raStrToDeg(raStr), raDeg, 4)

    def testDecStrToRad(self):
        for i in range(self.num):
            decDeg = self.goodData[i][self.decDegCol]
            decRad = decDeg*math.pi/180
            decStr = self.goodData[i][self.decStrCol]
            self.assertAlmostEqual(lsstutils.decStrToRad(decStr), decRad, 4)

    def testDecStrToDeg(self):
        for i in range(self.num):
            decDeg = self.goodData[i][self.decDegCol]
            decStr = self.goodData[i][self.decStrCol]
            self.assertAlmostEqual(lsstutils.decStrToDeg(decStr), decDeg, 3)


class TestMemory(lsst.utils.tests.MemoryTestCase):
    pass


def setup_module(module):
    lsst.utils.tests.init()

if __name__ == "__main__":
    setup_module(sys.modules[__name__])
    unittest.main()
