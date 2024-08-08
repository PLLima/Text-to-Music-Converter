'''
Created on 2024-07-11

@author: Pedro Lubaszewski Lima

This file contains the classes related to the main header widget of the application.
'''

from common.classes import Child
from common.dictionaries import FONTS
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

class title(ttk.Frame, Child):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.setParent(parent)
        self.__setInstance()

    def __setInstance(self):
        self.__instance = tk.Label(self.getParent(), justify='center', cursor='xterm')

    def getInstance(self):
        return self.__instance

    def setContent(self, content):
        self.getInstance().configure(text=content)

    def getContent(self):
        return self.getInstance().cget("text")

    def setFont(self, font):
        self.__font = font
        self.getInstance().configure(font=self.__font)

    def getFont(self):
        return self.__font

class mainHeader(title):
    def __init__(self, parent):
        super().__init__(parent)

    def setFontSize(self, fontSize):
        font = tkFont.Font(family=FONTS["MainHeader"], size=fontSize, weight='bold')
        self.setFont(font)

    def getFontSize(self):
        return self.getFont().actual()["size"]

class mainSubtitle(title):
    def __init__(self, parent):
        super().__init__(parent)

    def setFontSize(self, fontSize):
        font = tkFont.Font(family=FONTS["MainSubtitle"], size=fontSize)
        self.setFont(font)

    def getFontSize(self):
        return self.getFont().actual()["size"]
    
class screenTitle(title):
    def __init__(self, parent):
        super().__init__(parent)

    def setFontSize(self, fontSize):
        font = tkFont.Font(family=FONTS["ScreenTitle"], size=fontSize, weight='bold')
        self.setFont(font)

    def getFontSize(self):
        return self.getFont().actual()["size"]