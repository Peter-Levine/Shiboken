#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the Shiboken Python Bindings Generator project.
#
# Copyright (C) 2009 Nokia Corporation and/or its subsidiary(-ies).
#
# Contact: PySide team <contact@pyside.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# version 2.1 as published by the Free Software Foundation. Please
# review the following information to ensure the GNU Lesser General
# Public License version 2.1 requirements will be met:
# http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
# #
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301 USA

'''Test cases for Python representation of C++ enums.'''

import unittest

from sample import SampleNamespace

class EnumTest(unittest.TestCase):
    '''Test case for Python representation of C++ enums.'''

    def testEnumValuesInsideEnum(self):
        '''Enum values should be accessible inside the enum as well as outside.'''
        for value_name in SampleNamespace.Option.values:
            enum_item1 = getattr(SampleNamespace.Option, value_name)
            enum_item2 = getattr(SampleNamespace, value_name)
            self.assertEqual(enum_item1, enum_item2)

    def testPassingIntegerOnEnumArgument(self):
        '''Tries to use an integer in place of an enum argument.'''
        self.assertRaises(TypeError, SampleNamespace.getNumber, 1)

    def testBuildingEnumFromIntegerValue(self):
        '''Tries to build the proper enum using an integer.'''
        SampleNamespace.getNumber(SampleNamespace.Option(1))

    def testBuildingEnumWithDefaultValue(self):
        '''Enum constructor with default value'''
        enum = SampleNamespace.Option()
        self.assertEqual(enum, SampleNamespace.None)

    def testEnumConversionToAndFromPython(self):
        '''Conversion of enum objects from Python to C++ back again.'''
        enumout = SampleNamespace.enumInEnumOut(SampleNamespace.TwoIn)
        self.assert_(enumout, SampleNamespace.TwoOut)

    def testEnumConstructorWithTooManyParameters(self):
        '''Calling the constructor of non-extensible enum with the wrong number of parameters.'''
        self.assertRaises(TypeError, SampleNamespace.InValue, 13, 14)

    def testEnumConstructorWithNonNumberParameter(self):
        '''Calling the constructor of non-extensible enum with a string.'''
        self.assertRaises(TypeError, SampleNamespace.InValue, '1')

if __name__ == '__main__':
    unittest.main()
