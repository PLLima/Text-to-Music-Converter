from tkinter import ttk

from common.classes import Screen
from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES, BUTTON_COLORS
from common.widgets.title import mainHeader, mainSubtitle
from common.widgets.button import textButton

class startScreen(ttk.Frame, Screen):
    def __init__(self, appController):
        self.setParent(appController.getParent())
        ttk.Frame.__init__(self, self.getParent())
        self.setAppController(appController)

    def __setTextsFrame(self, title, subtitle):
        self.__textsFrame = ttk.Frame(self)

        header = mainHeader(self.__getTextsFrame())
        header.setFontSize(calculateFontSize(TEXT_SCALES["MainHeader"], self.getAppController().getScreenSize()))
        header.setContent(title)
        header.getInstance().pack(pady=25)

        subheader = mainSubtitle(self.__getTextsFrame())
        subheader.setFontSize(calculateFontSize(TEXT_SCALES["MainSubtitle"], self.getAppController().getScreenSize()))
        subheader.setContent(subtitle)
        subheader.getInstance().pack(pady=[0, 90])

    def __getTextsFrame(self):
        return self.__textsFrame

    def __setButtonsFrame(self, textButton1, commandButton1, textButton2, commandButton2):
        self.__buttonsFrame = ttk.Frame(self)

        self.__getButtonsFrame().grid_rowconfigure(0, weight=1)
        self.__getButtonsFrame().grid_columnconfigure((0, 1), weight=1)

        getStartedButton = textButton(self.__getButtonsFrame(), commandButton1)
        getStartedButton.setText(textButton1, calculateFontSize(TEXT_SCALES["TextButton"], self.getAppController().getScreenSize()))
        getStartedButton.setBackgroundColor(BUTTON_COLORS["Red"])
        getStartedButton.setPadding(padx=45, pady=10)
        getStartedButton.getInstance().grid(row=0, column=0, sticky="E", padx=25)

        learnMoreButton = textButton(self.__getButtonsFrame(), commandButton2)
        learnMoreButton.setText(textButton2, calculateFontSize(TEXT_SCALES["TextButton"], self.getAppController().getScreenSize()))
        learnMoreButton.setBackgroundColor(BUTTON_COLORS["Black"])
        learnMoreButton.setPadding(padx=50, pady=10)
        learnMoreButton.getInstance().grid(row=0, column=1, sticky="W", padx=25)

    def __getButtonsFrame(self):
        return self.__buttonsFrame

    def render(self):
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.__setTextsFrame('Turn Text into Music', 'Create beautiful melodies from your words')
        self.__setButtonsFrame('Get Started', None,
                               'Learn More', lambda: self.switchScreen(self.getAppController().renderLearnScreen()))

        self.__getTextsFrame().grid(row=0, column=0, sticky="S")
        self.__getButtonsFrame().grid(row=1, column=0, sticky="N")
        self.pack(expand=True, fill='both')