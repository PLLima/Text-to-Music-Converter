'''
Created on 2024-06-28

@author: Pedro Lubaszewski Lima

This is the first screen that opens at the start of the application.
'''

import tkinter as tk
from tkinter import ttk

class start_screen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def render(self):
        self.parent.wm_title("Text to Music Converter")
        # tk.Label(root, text = 'Text to Music Converter').pack()

        frm = ttk.Frame(self.parent, padding = 10)
        frm.grid()
        ttk.Label(frm, text = "Hello World").grid(column = 0, row = 0)
        ttk.Button(frm, text = "Quit", command = self.parent.destroy).grid(column = 1, row = 0)

        self.parent.mainloop()