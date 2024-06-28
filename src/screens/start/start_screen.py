'''
Created on 2024-06-28

@author: Pedro Lubaszewski Lima

This is the first screen that opens at the start of the application.
'''

import tkinter as tk
from tkinter import ttk

def render():
    root = tk.Tk()
    tk.Label(root, text = 'Text to Music Converter').pack

    root.mainloop()

def test():
    render()
if __name__ == '__main__':
    test()