'''
Created on 2024-06-28

@author: Pedro Lubaszewski Lima

This is the starting point of the application, to where every major module is imported.
'''

import re
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

    def setMinAppScreenSize(self, minSize):
        splitMinSize = re.split('x', minSize)

        self.appMinScreenSize = minSize
        self.parent.minsize(splitMinSize[0], splitMinSize[1])

    def getMinAppScreenSize(self):
        return self.appMinScreenSize

    def setAppScreenSize(self, size):
        self.appScreenSize = size
        self.parent.geometry(size)

    def getAppScreenSize(self):
        return self.appScreenSize

    def begin(self):
        # Starting point of the application
        startScreen(self.parent).render()

def main():
    minScreenSize = ['400', '200']
    initialScreenSize = ['400', '200']
    root = tk.Tk()

    # Set main screen parameters
    app = mainApplication(root)
    app.setAppName("Text to Music Converter")
    app.setAppScreenSize("x".join(initialScreenSize))
    app.setMinAppScreenSize("x".join(minScreenSize))
    
    app.begin()
    root.mainloop()

if __name__ == '__main__':
    main()