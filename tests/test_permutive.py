#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_permutive
----------------------------------

Tests for `permutive` module.
"""


import sys
import unittest

from permutive import Permutive


class TestPermutive(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_permutive(self):
        permutive = Permutive('12345')
        self.assertTrue(isinstance(permutive, Permutive))
