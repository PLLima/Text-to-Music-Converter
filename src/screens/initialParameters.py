import tkinter as tk
from tkinter import ttk

from common.classes import Screen
from common.functions import calculateFontSize
from common.dictionaries import SCREEN_COLORS, TEXT_SCALES, TEXTBOX_PARAMS, BUTTON_COLORS
from common.widgets.screenHeader import screenHeader
from common.widgets.button import textButton
from common.widgets.textbox import textbox
from common.widgets.textboxCounter import textboxCounter

class paramsScreen(tk.Frame, Screen):
    def __init__(self, appController):
        self.setParent(appController.getParent())
        tk.Frame.__init__(self, self.getParent(), bg=SCREEN_COLORS["Background"])
        self.setAppController(appController)

    def __setTextbox(self, parent, placeholder, maxCharacters, keyPressedFunction):
        self.__textInput = textbox(parent, placeholder, maxCharacters, keyPressedFunction)

    def __getTextbox(self):
        return self.__textInput

    def __setTextButtonFrame(self, textButton1, commandButton1, maxCharacters):
        self.__textButtonFrame = tk.Frame(self.__getTextOptionsFrame(), bg=SCREEN_COLORS["Background"], borderwidth=2, relief='solid')

        self.__getTextButtonFrame().grid_rowconfigure(0, weight=1)
        self.__getTextButtonFrame().grid_columnconfigure((0, 1), weight=1, uniform="column")

        importButton = textButton(self.__getTextButtonFrame(), commandButton1)
        importButton.setText(textButton1, calculateFontSize(TEXT_SCALES["ImportButton"], self.getAppController().getScreenSize()))
        importButton.setBackgroundColor(BUTTON_COLORS["Red"])
        importButton.setPadding(padx=25, pady=3)
        importButton.getInstance().grid(row=0, column=0, sticky="W", pady=8)

        characterCounter = textboxCounter(self.__getTextButtonFrame(), maxCharacters)
        characterCounter.setFontSize(calculateFontSize(TEXT_SCALES["TextboxCounter"], self.getAppController().getScreenSize()))
        characterCounter.setCounter(len(self.__getTextbox().getContent()) - 1)
        characterCounter.grid(row=0, column=1, sticky="E", padx=5, pady=8)

    def __getTextButtonFrame(self):
        return self.__textButtonFrame

    def __setTextOptionsFrame(self, textboxPlaceholder, maxCharacters, importCommand):
        self.__textOptionsFrame = tk.Frame(self, bg=SCREEN_COLORS["Background"], borderwidth=2, relief='solid')

        self.__getTextOptionsFrame().grid_rowconfigure((0, 1), weight=1)
        self.__getTextOptionsFrame().grid_columnconfigure(0, weight=1)

        self.__setTextbox(self.__getTextOptionsFrame(), textboxPlaceholder, maxCharacters, None)
        self.__getTextbox().setHeight(9)
        self.__getTextbox().setWidth(105)
        self.__getTextbox().setFontSize(calculateFontSize(TEXT_SCALES["ParamsScreenTextbox"], self.getAppController().getScreenSize()))
        self.__getTextbox().grid(row=0, column=0, sticky="N", ipady=10)

        self.__setTextButtonFrame('Import', importCommand, maxCharacters)
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