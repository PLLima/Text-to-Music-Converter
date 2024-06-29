'''
Created on 2024-06-28

@author: Pedro Lubaszewski Lima

This is the starting point of the application, to where every major module is imported.
'''

import tkinter as tk
from screens.start import start_screen

class main_application(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def begin(self):
        start_screen(self.parent).render()

def main():
    root = tk.Tk()
    main_application(root).begin()
    root.mainloop()

if __name__ == '__main__':
    main()