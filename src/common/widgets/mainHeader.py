'''
Created on 2024-07-11

@author: Pedro Lubaszewski Lima

This file contains the classes related to the main header widget of the application.
'''

from common.classes import Child
from common.dictionaries import FONTS
import tkinter as tk

class mainHeader(tk.Frame, Child):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.setParent(parent)
        self.setInstance()

    def setInstance(self):
        self.instance = tk.Label(self.getParent(), justify='center')

    def getInstance(self):
        return self.instance

    def setContent(self, content):
        self.getInstance().configure(text=content)

    def setFontSize(self, fontSize):
        self.getInstance().configure(font=(FONTS["MainHeader"], fontSize))

    def render(self):
        self.getInstance().pack(side='top', fill='both', expand=True)