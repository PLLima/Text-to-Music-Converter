import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

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

    def __setImportButton(self, parent, command):
        self.__importButton = textButton(parent, command)

    def __getImportButton(self):
        return self.__importButton

    def __getCharacterCounter(self):
        return self.__characterCounter

    def __setCharacterCounter(self, parent, maxCharacters):
        self.__characterCounter = textboxCounter(parent, maxCharacters)

    def __getCharacterCounter(self):
        return self.__characterCounter

    def __checkTextboxCharacter(self, event, *args):
        self.__getCharacterCounter().setCounter(len(self.__getTextbox().getContent()) - 1)

    def __openTextFile(self, maxCharacters):
        file = fd.askopenfile(mode='r', title='Open a text file', initialdir='./', filetypes=[('Text files', '*.txt')])
        if file != None:
            text = file.read()
            if len(text) > maxCharacters:
                text = text[:maxCharacters]
            if text != '':
                self.__getTextbox().setContent(text)
                self.__getTextbox().enable()
                self.__getCharacterCounter().setCounter(len(text))

    def __setTextButtonFrame(self, textButton1, commandButton1, maxCharacters):
        self.__textButtonFrame = tk.Frame(self.__getTextOptionsFrame(), bg=SCREEN_COLORS["Background"])

        self.__getTextButtonFrame().grid_rowconfigure(0, weight=1)
        self.__getTextButtonFrame().grid_columnconfigure((0, 1), weight=1, uniform="column")

        self.__setImportButton(self.__getTextButtonFrame(), commandButton1)
        self.__getImportButton().setText(textButton1, calculateFontSize(TEXT_SCALES["ImportButton"], self.getAppController().getScreenSize()))
        self.__getImportButton().setBackgroundColor(BUTTON_COLORS["Red"])
        self.__getImportButton().setPadding(padx=25, pady=3)
        self.__getImportButton().getInstance().grid(row=0, column=0, sticky="W", pady=6)

        self.__setCharacterCounter(self.__getTextButtonFrame(), maxCharacters)
        self.__getCharacterCounter().setFontSize(calculateFontSize(TEXT_SCALES["TextboxCounter"], self.getAppController().getScreenSize()))
        self.__getCharacterCounter().setCounter(0)
        self.__getCharacterCounter().grid(row=0, column=1, sticky="E", padx=20, pady=6)

    def __getTextButtonFrame(self):
        return self.__textButtonFrame

    def __setTextOptionsFrame(self, textboxPlaceholder, maxCharacters, importCommand):
        self.__textOptionsFrame = tk.Frame(self, bg=SCREEN_COLORS["Background"])

        self.__getTextOptionsFrame().grid_rowconfigure((0, 1), weight=1)
        self.__getTextOptionsFrame().grid_columnconfigure(0, weight=1)

        self.__setTextbox(self.__getTextOptionsFrame(), textboxPlaceholder, maxCharacters, self.__checkTextboxCharacter)
        self.__getTextbox().setHeight(9)
        self.__getTextbox().setWidth(105)
        self.__getTextbox().setFontSize(calculateFontSize(TEXT_SCALES["ParamsScreenTextbox"], self.getAppController().getScreenSize()))
        self.__getTextbox().grid(row=0, column=0, sticky="S")

        self.__setTextButtonFrame('Import', importCommand, maxCharacters)
        self.__getTextButtonFrame().grid(row=1, column=0, sticky="NEW", padx=46)

    def __getTextOptionsFrame(self):
        return self.__textOptionsFrame

    def render(self):
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = screenHeader(self, lambda: self.switchScreen(self.getAppController().renderStartScreen()), 'Initial Parameters',
                              self.getAppController().getScreenSize())
        
        self.__setTextOptionsFrame('Insert your text here.', TEXTBOX_PARAMS["MaxCharacters"], lambda: self.__openTextFile(TEXTBOX_PARAMS["MaxCharacters"]))

        header.grid(row=0, column=0, sticky="NEW", pady=20)
        self.__getTextOptionsFrame().grid(row=1, column=0, sticky="NEW")
        self.pack(expand=True, fill='both')