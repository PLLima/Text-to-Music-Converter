import unittest

import tkinter as tk
from src.main import mainApplication
from src.controller import appController
from src.screens.start import startScreen

class testStartScreen(unittest.TestCase):
    def setUp(self):
        initialScreenSize = ['120', '120']
        root = tk.Tk()
        app = mainApplication(root)
        app.setAppScreenSize(initialScreenSize)
        controller = appController(app)
        self.startScreen = startScreen(controller)

    def testRender(self):
        self.startScreen.render()
        self.startScreen.getParent().update()
        self.assertTrue(self.startScreen.winfo_exists(), "Start screen wasn't rendered.")

if __name__ == '__main__':
    unittest.main()