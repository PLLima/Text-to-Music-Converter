from tkinter import ttk

from common.classes import Child
from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES, BUTTON_COLORS
from common.widgets.title import mainHeader, mainSubtitle
from common.widgets.button import textButton

class startScreen(ttk.Frame, Child):
    def __init__(self, appController):
        self.setParent(appController.getParent())
        ttk.Frame.__init__(self, self.getParent())
        self.__setAppController(appController)

    def __setAppController(self, appController):
        self.__appController = appController

    def __getAppController(self):
        return self.__appController

    def switchScreen(self, nextScreen):
        nextScreen
        self.destroy()

    def render(self):
        textsFrame = ttk.Frame(self)
        buttonsFrame = ttk.Frame(self)

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)

        title = mainHeader(textsFrame)
        title.setFontSize(calculateFontSize(TEXT_SCALES["MainHeader"], self.__getAppController().getScreenSize()))
        title.setContent('Turn Text into Music')
        title.getInstance().pack(pady=25)

        subtitle = mainSubtitle(textsFrame)
        subtitle.setFontSize(calculateFontSize(TEXT_SCALES["MainSubtitle"], self.__getAppController().getScreenSize()))
        subtitle.setContent('Create beautiful melodies from your words')
        subtitle.getInstance().pack(pady=[0, 90])

        buttonsFrame.grid_rowconfigure(0, weight=1)
        buttonsFrame.grid_columnconfigure((0, 1), weight=1)

        getStartedButton = textButton(buttonsFrame, lambda: self.switchScreen(self.__getStartScreen))
        getStartedButton.setText('Get Started', calculateFontSize(TEXT_SCALES["TextButton"], self.__getAppController().getScreenSize()))
        getStartedButton.setBackgroundColor(BUTTON_COLORS["Red"])
        getStartedButton.setPadding(padx=45, pady=10)
        getStartedButton.getInstance().grid(row=0, column=0, sticky="E", padx=25)

        learnMoreButton = textButton(buttonsFrame, lambda: self.switchScreen(self.__getAppController().renderLearnScreen()))
        learnMoreButton.setText('Learn More', calculateFontSize(TEXT_SCALES["TextButton"], self.__getAppController().getScreenSize()))
        learnMoreButton.setBackgroundColor(BUTTON_COLORS["Black"])
        learnMoreButton.setPadding(padx=50, pady=10)
        learnMoreButton.getInstance().grid(row=0, column=1, sticky="W", padx=25)

        textsFrame.grid(row=0, column=0, sticky="S")
        buttonsFrame.grid(row=1, column=0, sticky="N")
        self.pack(expand=True, fill='both')
