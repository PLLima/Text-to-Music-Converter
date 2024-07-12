'''
Created on 2024-06-28

@author: Pedro Lubaszewski Lima

This is the first screen that opens at the start of the application.
'''

from common.classes import Child
from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES
from common.widgets.mainHeader import mainHeader
from common.widgets.mainSubtitle import mainSubtitle
from tkinter import ttk

class startScreen(ttk.Frame, Child):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.setParent(parent)

    # def __writeTitle(self, title):
    #     screenSize = self.getParent().getAppScreenSize()
    #     mainTitle = mainHeader(self.getParent().getParent())
    #     mainTitle.setFontSize(calculateFontSize(TEXT_SCALES["MainHeader"], screenSize))
    #     mainTitle.setContent(title)
    #     mainTitle.render()

    def render(self):
        mainFrame = ttk.Frame(self.getParent().getParent())
        textsFrame = ttk.Frame(mainFrame)
        buttonsFrame = ttk.Frame(mainFrame)
        # Center widgets inside main frame
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)

        screenSize = self.getParent().getAppScreenSize()
        title = mainHeader(textsFrame)
        title.setFontSize(calculateFontSize(TEXT_SCALES["MainHeader"], screenSize))
        title.setContent('Turn Text into Music')
        title.render()

        subtitle = mainSubtitle(textsFrame)
        subtitle.setFontSize(calculateFontSize(TEXT_SCALES["MainSubtitle"], screenSize))
        subtitle.setContent('Create beautiful melodies from your words')
        subtitle.render()

        textsFrame.grid(row=0, column=0, sticky="")
        buttonsFrame.grid(row=0, column=0, sticky="")
        mainFrame.pack(expand=True, fill='both')
        # self.__writeTitle('Turn Text into Music')

        # frm = ttk.Frame(self.parent, padding = 10)
        # frm.grid()
        # ttk.Label(frm, text = "Hello World").grid(column = 0, row = 0)
        # ttk.Button(frm, text = "Quit", command = self.parent.destroy).grid(column = 1, row = 0)