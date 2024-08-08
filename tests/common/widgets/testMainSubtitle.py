'''
Created on 2024-07-12

@author: Pedro Lubaszewski Lima

File with automated unit tests for the mainSubtitle widget.
'''

import unittest

import tkinter as tk
from src.common.widgets.mainSubtitle import mainSubtitle

class testStartScreen(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.mainSubtitle = mainSubtitle(root)

    def testSetGetValidContent(self):
        subtitle = 'Testing...'
        self.mainSubtitle.setContent(subtitle)
        self.assertEqual(self.mainSubtitle.getContent(), subtitle, "Subtitle not set accordingly.")

    def testSetGetEmptyContent(self):
        subtitle = ''
        self.mainSubtitle.setContent(subtitle)
        self.assertEqual(self.mainSubtitle.getContent(), subtitle, "Empty subtitle not set accordingly.")

    def testSetGetValidFontSize(self):
        fontSize = 6
        self.mainSubtitle.setFontSize(fontSize)
        self.assertEqual(self.mainSubtitle.getFontSize(), fontSize, "Subtitle font size set incorrectly.")

if __name__ == '__main__':
    unittest.main()