'''
Created on 2024-07-02

@author: Pedro Lubaszewski Lima

File with automated unit tests for the startScreen class.
'''

import unittest

import tkinter as tk
from src.main import mainApplication
from src.screens.start import startScreen

class testStartScreen(unittest.TestCase):
    def setUp(self):
        initialScreenSize = ['120', '120']
        root = tk.Tk()
        mainApp = mainApplication(root)
        self.startScreen = startScreen(mainApp)
        self.startScreen.getParent().setAppScreenSize(initialScreenSize)

    def testRender(self):
        self.startScreen.render()
        self.startScreen.getParent().getParent().update()
        self.assertTrue(self.startScreen.winfo_exists(), "Start screen wasn't rendered.")

if __name__ == '__main__':
    unittest.main()