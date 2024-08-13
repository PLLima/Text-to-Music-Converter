import tkinter as tk
from tkinter import ttk

from common.classes import Child
from common.functions import calculateFontSize
from common.dictionaries import SCREEN_COLORS, TEXT_SCALES
from common.widgets.title import screenTitle
from common.widgets.button import backButton

class screenHeader(tk.Frame, Child):
    def __init__(self, parent, lastScreen, title, screenSize):
        tk.Frame.__init__(self, parent, bg=SCREEN_COLORS["Background"])
        self.setParent(parent)
        self.__setLastScreen(lastScreen)
        self.__setTitle(title)
    
        titleFrame = tk.Frame(self, bg=SCREEN_COLORS["Background"])

        self.grid_columnconfigure(0, weight=1, uniform='column')
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1, uniform='column')

        titleFrame.grid_rowconfigure(0, weight=1)
        titleFrame.grid_columnconfigure(0, weight=1)

        returnButton = backButton(self, self.__getLastScreen())
        returnButton.getInstance().grid(row=0, column=0, sticky="W", padx=45)

        title = screenTitle(titleFrame)
        title.setFontSize(calculateFontSize(TEXT_SCALES["ScreenTitle"], screenSize))
        title.setContent(self.__getTitle())
        title.getInstance().grid(row=0, column=1, sticky="NSEW")

        titleFrame.grid(row=0, column=1, sticky="")

    def __setLastScreen(self, lastScreen):
        self.__lastScreen = lastScreen
    
    def __getLastScreen(self):
        return self.__lastScreen
    
    def __setTitle(self, title):
        self.__title = title
    
    def __getTitle(self):
        return self.__title