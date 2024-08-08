'''
Created on 2024-06-28

@author: Pedro Lubaszewski Lima

This is the first screen that opens at the start of the application.
'''

from common.classes import Child
from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES
from common.dictionaries import BUTTON_COLORS
from common.widgets.title import mainHeader, mainSubtitle
from common.widgets.button import textButton
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
        mainFrame.grid_rowconfigure(1, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)

        screenSize = self.getParent().getAppScreenSize()
        title = mainHeader(textsFrame)
        title.setFontSize(calculateFontSize(TEXT_SCALES["MainHeader"], screenSize))
        title.setContent('Turn Text into Music')
        title.getInstance().pack(pady=25)

        subtitle = mainSubtitle(textsFrame)
        subtitle.setFontSize(calculateFontSize(TEXT_SCALES["MainSubtitle"], screenSize))
        subtitle.setContent('Create beautiful melodies from your words')
        subtitle.getInstance().pack(pady=[0, 90])

        buttonsFrame.grid_rowconfigure(0, weight=1)
        buttonsFrame.grid_columnconfigure(0, weight=1)
        buttonsFrame.grid_columnconfigure(1, weight=1)

        getStartedButton = textButton(buttonsFrame, None)
        getStartedButton.setText('Get Started', calculateFontSize(TEXT_SCALES["TextButton"], screenSize))
        getStartedButton.setBackgroundColor(BUTTON_COLORS["Red"])
        getStartedButton.setPadding(padx=45, pady=10)
        getStartedButton.getInstance().grid(row=0, column=0, sticky="E", padx=25)

        learnMoreButton = textButton(buttonsFrame, None)
        learnMoreButton.setText('Learn More', calculateFontSize(TEXT_SCALES["TextButton"], screenSize))
        learnMoreButton.setBackgroundColor(BUTTON_COLORS["Black"])
        learnMoreButton.setPadding(padx=50, pady=10)
        learnMoreButton.getInstance().grid(row=0, column=1, sticky="W", padx=25)

        textsFrame.grid(row=0, column=0, sticky="S")
        buttonsFrame.grid(row=1, column=0, sticky="N")
        mainFrame.pack(expand=True, fill='both')