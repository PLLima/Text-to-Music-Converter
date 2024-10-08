import unittest

import tkinter as tk
from src.common.dictionaries import SCREEN_MEASURE
from src.main import mainApplication

class testMainApplication(unittest.TestCase):
    def setUp(self):
        initialScreenSize = ['120', '120']
        root = tk.Tk()
        self.app = mainApplication(root)
        self.app.setAppScreenSize(initialScreenSize)

    def testGetAppName(self):
        self.app.setAppName("Test...")

        self.assertEqual(self.app.getAppName(), "Test...", "App name incorrect.")

    def testSetMinAppScreenSize(self):
        minScreenSize = ['400', '200']
        intendedScreenSize = ['200', '150']
        self.app.setMinAppScreenSize(minScreenSize)
        self.app.setAppScreenSize(intendedScreenSize)
        self.app.getParent().update()

        self.assertEqual(int(minScreenSize[SCREEN_MEASURE["Width"]]), self.app.getParent().winfo_width(), "App minimum screen width disrespected.")
        self.assertEqual(int(minScreenSize[SCREEN_MEASURE["Height"]]), self.app.getParent().winfo_height(), "App minimum screen height disrespected.")

    def testGetMinAppScreenSize(self):
        minScreenSize = ['120', '120']
        self.app.setMinAppScreenSize(minScreenSize)
        self.assertEqual(self.app.getMinAppScreenSize(), minScreenSize, "App minimum screen size incorrect.")

    def testSetMaxAppScreenSize(self):
        maxScreenSize = ['400', '200']
        intendedScreenSize = ['800', '300']
        self.app.setMaxAppScreenSize(maxScreenSize)
        self.app.setAppScreenSize(intendedScreenSize)
        self.app.getParent().update()

        self.assertEqual(int(maxScreenSize[SCREEN_MEASURE["Width"]]), self.app.getParent().winfo_width(), "App maximum screen width disrespected.")
        self.assertEqual(int(maxScreenSize[SCREEN_MEASURE["Height"]]), self.app.getParent().winfo_height(), "App maximum screen height disrespected.")

    def testGetMaxAppScreenSize(self):
        maxScreenSize = ['120', '120']
        self.app.setMaxAppScreenSize(maxScreenSize)
        self.assertEqual(self.app.getMaxAppScreenSize(), maxScreenSize, "App maximum screen size incorrect.")

    def testSetAppScreenSize(self):
        screenSize = ['120', '120']
        self.app.setAppScreenSize(screenSize)
        self.app.getParent().update()

        self.assertEqual(int(screenSize[SCREEN_MEASURE["Width"]]), self.app.getParent().winfo_width(), "App screen width incorrect.")
        self.assertEqual(int(screenSize[SCREEN_MEASURE["Height"]]), self.app.getParent().winfo_height(), "App screen height incorrect.")

    def testGetAppScreenSize(self):
        screenSize = ['100', '100']
        self.app.setAppScreenSize(screenSize)

    def testBegin(self):
        self.app.begin()
        self.app.getParent().update()
        self.assertTrue(self.app.winfo_exists(), "Main application wasn't rendered.")

if __name__ == '__main__':
    unittest.main()