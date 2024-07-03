'''
Created on 2024-07-02

@author: Pedro Lubaszewski Lima

File with automated unit tests for the startScreen class.
'''

import unittest

import tkinter as tk
from src.screens.start import startScreen

class testStartScreen(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.root = root
        self.app = startScreen(root)

    def testRender(self):
        self.app.render()
        self.app.update()
        self.assertTrue(self.app.winfo_exists(), "Start screen wasn't rendered.")

if __name__ == '__main__':
    unittest.main()