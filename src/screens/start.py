from tkinter import ttk

from common.classes import Child, Closeable
from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES, BUTTON_COLORS
from common.widgets.title import mainHeader, mainSubtitle
from common.widgets.button import textButton
from screens.learnMore import learnScreen

class startScreen(ttk.Frame, Child, Closeable):
    def __init__(self, parent, screenSize):
        ttk.Frame.__init__(self, parent)
        self.setParent(parent)
        self.__screenSize = screenSize

    def switchScreen(self, nextScreen):
        self.destroy()
        nextScreen.render()

    def render(self):
        textsFrame = ttk.Frame(self)
        buttonsFrame = ttk.Frame(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title = mainHeader(textsFrame)
        title.setFontSize(calculateFontSize(TEXT_SCALES["MainHeader"], self.__screenSize))
        title.setContent('Turn Text into Music')
        title.getInstance().pack(pady=25)

        subtitle = mainSubtitle(textsFrame)
        subtitle.setFontSize(calculateFontSize(TEXT_SCALES["MainSubtitle"], self.__screenSize))
        subtitle.setContent('Create beautiful melodies from your words')
        subtitle.getInstance().pack(pady=[0, 90])

        buttonsFrame.grid_rowconfigure(0, weight=1)
        buttonsFrame.grid_columnconfigure(0, weight=1)
        buttonsFrame.grid_columnconfigure(1, weight=1)

        getStartedButton = textButton(buttonsFrame, None)
        getStartedButton.setText('Get Started', calculateFontSize(TEXT_SCALES["TextButton"], self.__screenSize))
        getStartedButton.setBackgroundColor(BUTTON_COLORS["Red"])
        getStartedButton.setPadding(padx=45, pady=10)
        getStartedButton.getInstance().grid(row=0, column=0, sticky="E", padx=25)

        learnMoreButton = textButton(buttonsFrame, lambda: self.switchScreen(learnScreen(self.getParent(), self.__screenSize)))
        learnMoreButton.setText('Learn More', calculateFontSize(TEXT_SCALES["TextButton"], self.__screenSize))
        learnMoreButton.setBackgroundColor(BUTTON_COLORS["Black"])
        learnMoreButton.setPadding(padx=50, pady=10)
        learnMoreButton.getInstance().grid(row=0, column=1, sticky="W", padx=25)

        textsFrame.grid(row=0, column=0, sticky="S")
        buttonsFrame.grid(row=1, column=0, sticky="N")
        self.pack(expand=True, fill='both')
