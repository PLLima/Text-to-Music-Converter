'''
Created on 2024-06-29

@author: Pedro Lubaszewski Lima

File with automated unit tests for the mainApplication class.
'''

import unittest

import tkinter as tk
from src.utils.enums import ScreenMeasure
from src.main import mainApplication

class testMainApplication(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.root = root
        self.app = mainApplication(root)

    def testGetAppName(self):
        self.app.setAppName("Test...")

        self.assertEqual(self.app.getAppName(), "Test...", "App name incorrect.")

    def testSetMinAppScreenSize(self):
        minScreenSize = ['400', '200']
        intendedScreenSize = ['200', '150']
        self.app.setMinAppScreenSize(minScreenSize)
        self.app.setAppScreenSize(intendedScreenSize)
        self.root.update()

        self.assertEqual(int(minScreenSize[ScreenMeasure.WIDTH]), self.root.winfo_width(), "App minimum screen width disrespected.")
        self.assertEqual(int(minScreenSize[ScreenMeasure.HEIGHT]), self.root.winfo_height(), "App minimum screen height disrespected.")

    def testGetMinAppScreenSize(self):
        minScreenSize = ['120', '120']
        self.app.setMinAppScreenSize(minScreenSize)
        self.assertEqual(self.app.getMinAppScreenSize(), minScreenSize, "App minimum screen size incorrect.")

    def testSetAppScreenSize(self):
        screenSize = ['120', '120']
        self.app.setAppScreenSize(screenSize)
        self.root.update()

        self.assertEqual(int(screenSize[ScreenMeasure.WIDTH]), self.root.winfo_width(), "App screen width incorrect.")
        self.assertEqual(int(screenSize[ScreenMeasure.HEIGHT]), self.root.winfo_height(), "App screen height incorrect.")

    def testGetAppScreenSize(self):
        screenSize = ['100', '100']
        self.app.setAppScreenSize(screenSize)

        self.assertEqual(self.app.getAppScreenSize(), screenSize, "App screen size incorrect.")

if __name__ == '__main__':
    unittest.main()