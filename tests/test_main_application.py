'''
Created on 2024-06-29

@author: Pedro Lubaszewski Lima

File with automated unit tests for the main_application class.
'''

import unittest

import tkinter as tk
from src.main import main_application

class TestMainApplication(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.root = root
        self.app = main_application(root)

    def test_get_app_name(self):
        self.app.set_app_name("Test...")
        self.assertEqual(self.app.get_app_name(), "Test...", "App name incorrect.")

    def test_set_app_screen_size(self):
        screen_size = ["120", "120"]
        self.app.set_app_screen_size("x".join(screen_size))
        self.root.update()
        self.assertEqual(int(screen_size[0]), self.root.winfo_width(), "App screen width incorrect.")
        self.assertEqual(int(screen_size[1]), self.root.winfo_height(), "App screen height incorrect.")

    def test_get_app_screen_size(self):
        screen_size = ["100", "100"]
        self.app.set_app_screen_size("x".join(screen_size))
        self.assertEqual(self.app.get_app_screen_size(), "x".join(screen_size), "App screen size incorrect.")

if __name__ == '__main__':
    unittest.main()