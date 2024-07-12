'''
Created on 2024-06-28

@author: Pedro Lubaszewski Lima

This is the first screen that opens at the start of the application.
'''

from common.classes import Child
from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES
from common.widgets.mainHeader import mainHeader
from tkinter import ttk

class startScreen(ttk.Frame, Child):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.setParent(parent)

    def __writeTitle(self, title):
        screenSize = self.getParent().getAppScreenSize()

        mainTitle = mainHeader(self.getParent().getParent())
        mainTitle.setFontSize(calculateFontSize(TEXT_SCALES["MainHeader"], screenSize))
        mainTitle.setContent(title)

        mainTitle.render()

    def render(self):
        self.__writeTitle('Turn Text into Music')

        # frm = ttk.Frame(self.parent, padding = 10)
        # frm.grid()
        # ttk.Label(frm, text = "Hello World").grid(column = 0, row = 0)
        # ttk.Button(frm, text = "Quit", command = self.parent.destroy).grid(column = 1, row = 0)