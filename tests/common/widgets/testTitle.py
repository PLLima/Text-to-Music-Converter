import unittest

import tkinter as tk
from src.common.widgets.title import mainHeader, mainSubtitle, screenTitle

class testMainHeader(unittest.TestCase):
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

class testMainHeader(unittest.TestCase):
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

class testScreenTitle(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.screenTitle = screenTitle(root)

    def testSetGetValidContent(self):
        subtitle = 'Testing...'
        self.screenTitle.setContent(subtitle)
        self.assertEqual(self.screenTitle.getContent(), subtitle, "Screen title not set accordingly.")

    def testSetGetEmptyContent(self):
        subtitle = ''
        self.screenTitle.setContent(subtitle)
        self.assertEqual(self.screenTitle.getContent(), subtitle, "Screen title subtitle not set accordingly.")

    def testSetGetValidFontSize(self):
        fontSize = 6
        self.screenTitle.setFontSize(fontSize)
        self.assertEqual(self.screenTitle.getFontSize(), fontSize, "Screen title font size set incorrectly.")

if __name__ == '__main__':
    unittest.main()