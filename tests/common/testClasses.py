import unittest

import tkinter as tk
from tkinter import ttk
from src.common.classes import *

class testChild(unittest.TestCase):
    def setUp(self):
        self.parent = 'Test'
        self.child = Child()

    def testSetGetParent(self):
        self.child.setParent(self.parent)
        self.assertEqual(self.child.getParent(), self.parent, "Parent incorrectly setted.")

if __name__ == '__main__':
    unittest.main()