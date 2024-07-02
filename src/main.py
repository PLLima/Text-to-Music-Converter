'''
Created on 2024-06-28

@author: Pedro Lubaszewski Lima

This is the starting point of the application, to where every major module is imported.
'''

import tkinter as tk
from screens.start import startScreen

class mainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def setAppName(self, name):
        self.appName = name
        self.parent.wm_title(name)

    def getAppName(self):
        return self.appName
    
    def setAppScreenSize(self, size):
        self.appScreenSize = size
        self.parent.geometry(size)
    
    def getAppScreenSize(self):
        return self.appScreenSize

    def begin(self):
        # Starting point of the application
        startScreen(self.parent).render()

def main():
    root = tk.Tk()

    # Set main screen parameters
    app = mainApplication(root)
    app.setAppName("Text to Music Converter")
    app.setAppScreenSize("400x200")
    
    app.begin()
    root.mainloop()

if __name__ == '__main__':
    main()