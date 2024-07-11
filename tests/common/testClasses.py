'''
Created on 2024-07-10

@author: Pedro Lubaszewski Lima

File with automated unit tests for the classes inside the classes.py file.
'''

import unittest

from src.common.classes import *

class testChild(unittest.TestCase):
    def setUp(self):
        self.parent = 'Test'
        self.child = Child()

    def testSetParent(self):
        self.child.setParent(self.parent)
        self.assertEqual(self.child.parent, self.parent, "Parent incorrectly setted.")

    def testGetParent(self):
        self.child.setParent(self.parent)
        self.assertEqual(self.child.getParent(), self.parent, "Gotten incorrect parent.")

if __name__ == '__main__':
    unittest.main()