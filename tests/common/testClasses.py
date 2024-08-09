import unittest

import tkinter as tk
from tkinter import ttk
from src.common.classes import *
from src.main import mainApplication

class testChild(unittest.TestCase):
    def setUp(self):
        self.parent = 'Test'
        self.child = Child()

    def testSetGetParent(self):
        self.child.setParent(self.parent)
        self.assertEqual(self.child.getParent(), self.parent, "Parent incorrectly setted.")

class testCloseable(unittest.TestCase):
    def setUp(self):
        initialScreenSize = ['120', '120']
        root = tk.Tk()
        self.app = mainApplication(root)
        self.app.setAppScreenSize(initialScreenSize)

    def testClose(self):
        self.app.begin()
        self.app.close()
        self.assertFalse(self.app.winfo_exists(), "Screen widgets not destroyed.")

if __name__ == '__main__':
    unittest.main()