'''
Created on 2024-06-28

@author: Pedro Lubaszewski Lima

This is the first screen that opens at the start of the application.
'''

import tkinter as tk
from tkinter import ttk

class start_screen():

    def render():
        root = tk.Tk()
        root.wm_title("Text to Music Converter")
        # tk.Label(root, text = 'Text to Music Converter').pack()

        frm = ttk.Frame(root, padding = 10)
        frm.grid()
        ttk.Label(frm, text="Hello Worldsfaeafewfef!").grid(column = 0, row = 0)
        ttk.Button(frm, text="Quit", command = root.destroy).grid(column = 1, row = 0)

        root.mainloop()

def test():
    start_screen.render()
if __name__ == '__main__':
    test()