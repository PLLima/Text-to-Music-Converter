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

    def set_app_name(self, name):
        self.app_name = name
        self.parent.wm_title(name)

    def get_app_name(self):
        return self.app_name
    
    def set_app_screen_size(self, size):
        self.app_screen_size = size
        self.parent.geometry(size)
    
    def get_app_screen_size(self):
        return self.app_screen_size

    def begin(self):
        # Starting point of the application
        start_screen(self.parent).render()

def main():
    root = tk.Tk()

    # Set main screen parameters
    app = main_application(root)
    app.set_app_name("Text to Music Converter")
    app.set_app_screen_size("400x200")

    app.begin()
    root.mainloop()

if __name__ == '__main__':
    main()