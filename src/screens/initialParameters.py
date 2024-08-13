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

    def __setTextButtonFrame(self, textButton, commandButton):
        self.__textButton = ttk.Frame(self.__getTextOptionsFrame())

        self.__getTextButtonFrame().grid_rowconfigure(0, weight=1)
        self.__getTextButtonFrame().grid_columnconfigure((0, 1), weight=1, uniform='column')

    def __getTextButtonFrame(self):
        return self.__textButton

    def __setTextOptionsFrame(self, textboxPlaceholder, maxCharacters):
        self.__textOptionsFrame = ttk.Frame(self)

        self.__getTextOptionsFrame().grid_rowconfigure((0, 1), weight=1)
        self.__getTextOptionsFrame().grid_columnconfigure(0, weight=1)

        textInput = textbox(self.__getTextOptionsFrame(), textboxPlaceholder, maxCharacters)
        textInput.setHeight(9)
        textInput.setWidth(105)
        textInput.setFontSize(calculateFontSize(TEXT_SCALES["ParamsScreenTextbox"], self.getAppController().getScreenSize()))
        textInput.grid(row=0, column=0, sticky="S", ipady=10)

        self.__setTextButtonFrame('Import', None)
        self.__getTextButtonFrame().grid(row=1, column=0, sticky="N")

    def __getTextOptionsFrame(self):
        return self.__textOptionsFrame

    def render(self):
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = screenHeader(self, lambda: self.switchScreen(self.getAppController().renderStartScreen()), 'Initial Parameters',
                              self.getAppController().getScreenSize())
        
        self.__setTextOptionsFrame('Insert your text here.', TEXTBOX_PARAMS["MaxCharacters"])

        header.grid(row=0, column=0, sticky="NSEW", pady=20)
        self.__getTextOptionsFrame().grid(row=1, column=0, sticky="NSEW")
        self.pack(expand=True, fill='both')