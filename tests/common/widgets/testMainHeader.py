'''
Created on 2024-07-11

@author: Pedro Lubaszewski Lima

File with automated unit tests for the mainHeader widget.
'''

import unittest

import tkinter as tk
from src.common.widgets.mainHeader import mainHeader

class testStartScreen(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.mainHeader = mainHeader(root)

    def testSetGetValidContent(self):
        header = 'Testing...'
        self.mainHeader.setContent(header)
        self.assertEqual(self.mainHeader.getContent(), header, "Header not set accordingly.")

    def testSetGetEmptyContent(self):
        header = ''
        self.mainHeader.setContent(header)
        self.assertEqual(self.mainHeader.getContent(), header, "Empty header not set accordingly.")

    def testSetGetValidFontSize(self):
        fontSize = 6
        self.mainHeader.setFontSize(fontSize)
        self.assertEqual(self.mainHeader.getFontSize(), fontSize, "Header font size set incorrectly.")

if __name__ == '__main__':
    unittest.main()