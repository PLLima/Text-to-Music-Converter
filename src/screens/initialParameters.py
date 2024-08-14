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
from common.widgets.slider import paramSlider

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
        textboxContent = self.__getTextbox().getContent()
        contentLength = len(textboxContent) - 1
        self.__getCharacterCounter().setCounter(contentLength)
        if contentLength > 0:
            self.__getGenerateButton().enable()
        else:
            self.__getGenerateButton().disable()

    def __openTextFile(self, maxCharacters):
        file = fd.askopenfile(mode='r', title='Open a text file', initialdir='./', filetypes=[('Text files', '*.txt')])
        if file != None:
            text = file.read()
            if len(text) > maxCharacters:
                text = text[:maxCharacters]
            if text != '':
                self.__getGenerateButton().enable()
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
        self.__getTextbox().setWidth(95)
        self.__getTextbox().setFontSize(calculateFontSize(TEXT_SCALES["ParamsScreenTextbox"], self.getAppController().getScreenSize()))
        self.__getTextbox().grid(row=0, column=0, sticky="S")

        self.__setTextButtonFrame('Import', importCommand, maxCharacters)
        self.__getTextButtonFrame().grid(row=1, column=0, sticky="NEW", padx=101)

    def __getTextOptionsFrame(self):
        return self.__textOptionsFrame

    def __setVolumeSlider(self, parent, minValue, maxValue, initialValue):
        self.__volumeSlider = paramSlider(parent, minValue, maxValue, initialValue,
                                          calculateFontSize(TEXT_SCALES["ImportButton"], self.getAppController().getScreenSize()), True)

    def __getVolumeSlider(self):
        return self.__volumeSlider

    def __setOtherParamsFrame(self):
        self.__otherParamsFrame = tk.Frame(self, bg=SCREEN_COLORS["Background"])

        self.__getOtherParamsFrame().grid_rowconfigure((0, 1, 2), weight=1)
        self.__getOtherParamsFrame().grid_columnconfigure(0, weight=1)

        self.__setVolumeSlider(self.__getOtherParamsFrame(), 0, 100, 50)
        self.__getVolumeSlider().setTitleText('Volume', calculateFontSize(TEXT_SCALES["ImportButton"], self.getAppController().getScreenSize()))
        self.__getVolumeSlider().setTextPadding(40, 40)
        self.__getVolumeSlider().grid(row=0, column=0, sticky="NEW", padx=250)

    def __getOtherParamsFrame(self):
        return self.__otherParamsFrame

    def __setGenerateButton(self, parent, command):
        self.__generateButton = textButton(parent, command)

    def __getGenerateButton(self):
        return self.__generateButton

    def __setGenerateFrame(self, text, command):
        self.__generateFrame = tk.Frame(self, bg=SCREEN_COLORS["Background"])

        self.__setGenerateButton(self.__getGenerateFrame(), command)
        self.__getGenerateButton().setText(text, calculateFontSize(TEXT_SCALES["TextButton"], self.getAppController().getScreenSize()))
        self.__getGenerateButton().setBackgroundColor(BUTTON_COLORS["Red"])
        self.__getGenerateButton().setPadding(padx=60, pady=10)
        self.__getGenerateButton().getInstance().pack(pady=25)
        self.__getGenerateButton().disable()

    def __getGenerateFrame(self):
        return self.__generateFrame

    def __generateMusic(self):
        self.switchScreen(self.getAppController().renderPlayerScreen(50, 250, "C2", "ABUBLEABUBLEABULE"))

    def render(self):
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = screenHeader(self, lambda: self.switchScreen(self.getAppController().renderStartScreen()), 'Initial Parameters',
                              self.getAppController().getScreenSize())
        
        self.__setTextOptionsFrame('Insert your text here.', TEXTBOX_PARAMS["MaxCharacters"], lambda: self.__openTextFile(TEXTBOX_PARAMS["MaxCharacters"]))
        self.__setOtherParamsFrame()
        self.__setGenerateFrame('Generate Music', lambda: self.__generateMusic())

        header.grid(row=0, column=0, sticky="NEW", pady=20)
        self.__getTextOptionsFrame().grid(row=1, column=0, sticky="NEW")
        self.__getOtherParamsFrame().grid(row=2, column=0, sticky="NEW")
        self.__getGenerateFrame().grid(row=3, column=0, sticky="SEW")
        self.pack(expand=True, fill='both')