'''
Created on 2024-06-29

@author: Pedro Lubaszewski Lima

File with automated unit tests for the main_application class.
'''

import unittest

import tkinter as tk
from src.main import mainApplication

class testMainApplication(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.root = root
        self.app = mainApplication(root)

    def testGetAppName(self):
        self.app.setAppName("Test...")
        self.assertEqual(self.app.getAppName(), "Test...", "App name incorrect.")

    def testSetAppScreenSize(self):
        screenSize = ["120", "120"]
        self.app.setAppScreenSize("x".join(screenSize))
        self.root.update()
        self.assertEqual(int(screenSize[0]), self.root.winfo_width(), "App screen width incorrect.")
        self.assertEqual(int(screenSize[1]), self.root.winfo_height(), "App screen height incorrect.")

    def testGetAppScreenSize(self):
        screenSize = ["100", "100"]
        self.app.setAppScreenSize("x".join(screenSize))
        self.assertEqual(self.app.getAppScreenSize(), "x".join(screenSize), "App screen size incorrect.")

if __name__ == '__main__':
    unittest.main()