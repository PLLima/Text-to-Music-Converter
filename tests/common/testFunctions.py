'''
Created on 2024-07-11

@author: Pedro Lubaszewski Lima

File with automated unit tests for the functions inside the functions.py file.
'''

import unittest

from src.common.dictionaries import TEXT_SCALES, SCREEN_MEASURE
from src.common.functions import *

class testCalculateFontSize(unittest.TestCase):
    def setUp(self):
        self.nullScreenSize = ['0', '0']
        self.validScreenSize = ['200', '200']
        self.mainHeaderFontSize = int(TEXT_SCALES["MainHeader"] * int(self.validScreenSize[SCREEN_MEASURE["Height"]]))

    def testNull(self):
        self.assertEqual(0, calculateFontSize(5.3, self.nullScreenSize), "Font size should have been zero.")
        self.assertEqual(0, calculateFontSize(0, self.validScreenSize), "Font size should have been zero.")
        self.assertEqual(0, calculateFontSize(0, self.nullScreenSize), "Font size should have been zero.")

    def testValidScreenSize(self):
        self.assertEqual(self.mainHeaderFontSize, calculateFontSize(TEXT_SCALES["MainHeader"], self.validScreenSize), "Font size calculated incorrectly.")

if __name__ == '__main__':
    unittest.main()