import unittest

import tkinter as tk
from src.screens.start import startScreen

class testStartScreen(unittest.TestCase):
    def setUp(self):
        initialScreenSize = ['120', '120']
        root = tk.Tk()
        self.startScreen = startScreen(root, initialScreenSize)

    def testRender(self):
        self.startScreen.render()
        self.startScreen.getParent().update()
        self.assertTrue(self.startScreen.winfo_exists(), "Start screen wasn't rendered.")

if __name__ == '__main__':
    unittest.main()