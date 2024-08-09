from common.dictionaries import SCREEN_MEASURE
from common.classes import Child
import tkinter as tk
from tkinter import ttk
from screens.start import startScreen

class mainApplication(ttk.Frame, Child):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.setParent(parent)

    def setAppName(self, name):
        self.__appName = name
        self.getParent().wm_title(name)

    def getAppName(self):
        return self.__appName

    def setMinAppScreenSize(self, minSize):
        self.__appMinScreenSize = minSize
        self.getParent().minsize(minSize[SCREEN_MEASURE["Width"]], minSize[SCREEN_MEASURE["Height"]])

    def getMinAppScreenSize(self):
        return self.__appMinScreenSize

    def setMaxAppScreenSize(self, maxSize):
        self.__appMaxScreenSize = maxSize
        self.getParent().maxsize(maxSize[SCREEN_MEASURE["Width"]], maxSize[SCREEN_MEASURE["Height"]])

    def getMaxAppScreenSize(self):
        return self.__appMaxScreenSize

    def setAppScreenSize(self, size):
        self.__appScreenSize = size
        self.getParent().geometry("x".join(size))

    def getAppScreenSize(self):
        return self.__appScreenSize

    def begin(self):
        # Starting point of the application
        startScreen(self.getParent(), self.getAppScreenSize()).render()

def main():
    minScreenSize = ['1280', '720']
    maxScreenSize = ['1280', '720']
    root = tk.Tk()

    # Set main screen parameters
    app = mainApplication(root)
    app.setAppName('Text to Music Converter')
    app.setMinAppScreenSize(minScreenSize)
    app.setMaxAppScreenSize(maxScreenSize)
    app.setAppScreenSize(maxScreenSize)
    
    app.begin()
    root.mainloop()

if __name__ == '__main__':
    main()