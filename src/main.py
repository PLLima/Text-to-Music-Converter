'''
Created on 2024-06-28

@author: Pedro Lubaszewski Lima

This is the starting point of the application, to where every major module is imported.
'''

from common.dictionaries import SCREEN_MEASURE
from common.classes import Child
import tkinter as tk
from tkinter import ttk
from screens.start import startScreen
from screens.learnMore import learnScreen

class mainApplication(ttk.Frame, Child):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.setParent(parent)

    def setAppName(self, name):
        self.appName = name
        self.getParent().wm_title(name)

    def getAppName(self):
        return self.appName

    def setMinAppScreenSize(self, minSize):
        self.appMinScreenSize = minSize
        self.getParent().minsize(minSize[SCREEN_MEASURE["Width"]], minSize[SCREEN_MEASURE["Height"]])

    def getMinAppScreenSize(self):
        return self.appMinScreenSize

    def setAppScreenSize(self, size):
        self.appScreenSize = size
        self.getParent().geometry("x".join(size))

    def getAppScreenSize(self):
        return self.appScreenSize

    def begin(self):
        # Starting point of the application
        learnScreen(self).render()

def main():
    minScreenSize = ['720', '512']
    initialScreenSize = ['720', '512']
    root = tk.Tk()

    # Set main screen parameters
    app = mainApplication(root)
    app.setAppName('Text to Music Converter')
    app.setAppScreenSize(initialScreenSize)
    app.setMinAppScreenSize(minScreenSize)
    
    app.begin()
    root.mainloop()

if __name__ == '__main__':
    main()