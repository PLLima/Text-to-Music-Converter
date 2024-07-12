'''
Created on 2024-07-12

@author: Pedro Lubaszewski Lima

This file contains the classes related to the main subtitle widget of the application.
'''

from common.classes import Child
from common.dictionaries import FONTS
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

class mainSubtitle(ttk.Frame, Child):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.setParent(parent)
        self.__setInstance()

    def __setInstance(self):
        self.instance = tk.Label(self.getParent(), justify='center')

    def __getInstance(self):
        return self.instance

    def setContent(self, content):
        self.__getInstance().configure(text=content)

    def getContent(self):
        return self.__getInstance().cget("text")

    def setFontSize(self, fontSize):
        self.font = tkFont.Font(family=FONTS["MainSubtitle"], size=fontSize)
        self.__getInstance().configure(font=self.font)

    def getFontSize(self):
        return self.font.actual()["size"]

    def render(self):
        self.__getInstance().pack(fill='both', pady=[0, 60])