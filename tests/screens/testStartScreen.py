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
        self.app = startScreen(mainApp)
        self.app.getParent().setAppScreenSize(initialScreenSize)

    def testRender(self):
        self.app.render()
        self.app.getParent().getParent().update()
        self.assertTrue(self.app.winfo_exists(), "Start screen wasn't rendered.")

if __name__ == '__main__':
    unittest.main()