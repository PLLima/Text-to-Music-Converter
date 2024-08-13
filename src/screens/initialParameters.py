from tkinter import ttk

from common.classes import Screen
from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES, TEXTBOX_PARAMS, BUTTON_COLORS
from common.widgets.screenHeader import screenHeader
from common.widgets.button import textButton
from common.widgets.textbox import textbox

class paramsScreen(ttk.Frame, Screen):
    def __init__(self, appController):
        self.setParent(appController.getParent())
        ttk.Frame.__init__(self, self.getParent())
        self.setAppController(appController)

    def __setTextbox(self, parent, placeholder, maxCharacters):
        self.__textInput = textbox(parent, placeholder, maxCharacters)

    def __getTextbox(self):
        return self.__textInput

    def __setTextButtonFrame(self, textButton1, commandButton1):
        self.__textButtonFrame = ttk.Frame(self.__getTextOptionsFrame())

        self.__getTextButtonFrame().grid_rowconfigure(0, weight=1)
        self.__getTextButtonFrame().grid_columnconfigure((0, 1), weight=1, uniform='column')

        importButton = textButton(self.__getTextButtonFrame(), commandButton1)
        importButton.setText(textButton1, calculateFontSize(TEXT_SCALES["ImportButton"], self.getAppController().getScreenSize()))
        importButton.setBackgroundColor(BUTTON_COLORS["Red"])
        importButton.setPadding(padx=25, pady=3)
        importButton.getInstance().grid(row=0, column=0, sticky="E", pady=8)

    def __getTextButtonFrame(self):
        return self.__textButtonFrame

    def __setTextOptionsFrame(self, textboxPlaceholder, maxCharacters, importCommand):
        self.__textOptionsFrame = ttk.Frame(self)

        self.__getTextOptionsFrame().grid_rowconfigure((0, 1), weight=1)
        self.__getTextOptionsFrame().grid_columnconfigure(0, weight=1)

        self.__setTextbox(self.__getTextOptionsFrame(), textboxPlaceholder, maxCharacters)
        self.__getTextbox().setHeight(9)
        self.__getTextbox().setWidth(105)
        self.__getTextbox().setFontSize(calculateFontSize(TEXT_SCALES["ParamsScreenTextbox"], self.getAppController().getScreenSize()))
        self.__getTextbox().grid(row=0, column=0, sticky="S", ipady=10)

        self.__setTextButtonFrame('Import', importCommand)
        self.__getTextButtonFrame().grid(row=1, column=0, sticky="N")

    def __getTextOptionsFrame(self):
        return self.__textOptionsFrame

    def render(self):
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = screenHeader(self, lambda: self.switchScreen(self.getAppController().renderStartScreen()), 'Initial Parameters',
                              self.getAppController().getScreenSize())
        
        self.__setTextOptionsFrame('Insert your text here.', TEXTBOX_PARAMS["MaxCharacters"], None)

        header.grid(row=0, column=0, sticky="NSEW", pady=20)
        self.__getTextOptionsFrame().grid(row=1, column=0, sticky="NSEW")
        self.pack(expand=True, fill='both')