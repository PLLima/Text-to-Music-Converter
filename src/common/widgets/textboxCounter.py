from common.classes import Child
from common.dictionaries import FONTS
from common.dictionaries import SCREEN_COLORS, TEXTBOXCOUNTER_COLORS
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

class textboxCounter(tk.Frame, Child):
    def __init__(self, parent, maxCharacters):
        tk.Frame.__init__(self, parent, bg=SCREEN_COLORS["Background"])
        self.setParent(parent)
        self.__setInstance()
        self.__setMaxCharacters(maxCharacters)
        self.__setForegroundColor(TEXTBOXCOUNTER_COLORS["Foreground"])
        self.getInstance().pack(expand=True, fill='both')

    def __setInstance(self):
        self.__instance = tk.Label(self, bg=SCREEN_COLORS["Background"], borderwidth=0, highlightthickness=0)

    def getInstance(self):
        return self.__instance

    def __setMaxCharacters(self, maxCharacters):
        self.__maxCharacters = maxCharacters
    
    def __getMaxCharacters(self):
        return self.__maxCharacters

    def __setForegroundColor(self, foregroundColor):
        self.getInstance().configure(fg=foregroundColor)

    def __getForegroundColor(self):
        return self.getInstance().cget("fg")

    def __setFont(self, font):
        self.__font = font
        self.getInstance().configure(font=self.__font)

    def __getFont(self):
        return self.__font
    
    def setFontSize(self, fontSize):
        font = tkFont.Font(family=FONTS["TextboxCounter"], size=fontSize)
        self.__setFont(font)

    def getFontSize(self):
        return self.__getFont().actual()["size"]
    
    def setCounter(self, characterCount):
        if characterCount == self.__getMaxCharacters():
            self.__setForegroundColor(TEXTBOXCOUNTER_COLORS["ForegroundMaxCharacters"])
        else:
            self.__setForegroundColor(TEXTBOXCOUNTER_COLORS["Foreground"])
        self.getInstance().configure(text=str(characterCount) + ' / ' + str(self.__getMaxCharacters()))