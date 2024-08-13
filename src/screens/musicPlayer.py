import tkinter as tk
from tkinter import ttk

from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES, BUTTON_COLORS, FONTS

from common.widgets.button import textButton
from common.classes import Screen
from common.widgets.screenHeader import screenHeader
from common.widgets.paramBoxGroup import paramBoxGroup

class playerScreen(ttk.Frame, Screen):
    def __init__(self, appController):
        self.setParent(appController.getParent())
        ttk.Frame.__init__(self, self.getParent())
        self.setAppController(appController)

    def __setButtonsFrame(self, textButton1, commandButton1, textButton2, commandButton2):
        self.__buttonsFrame = ttk.Frame(self)

        self.__getButtonsFrame().grid_rowconfigure(0, weight=1)
        self.__getButtonsFrame().grid_columnconfigure((0, 1), weight=1)

        playTrackButton = textButton(self.__getButtonsFrame(), commandButton1)
        playTrackButton.setText(textButton1, calculateFontSize(TEXT_SCALES["TextButton"], self.getAppController().getScreenSize()))
        playTrackButton.setBackgroundColor(BUTTON_COLORS["Red"])
        playTrackButton.setPadding(padx=45, pady=10)
        playTrackButton.getInstance().grid(row=0, column=0, sticky="E", padx=25)

        downloadButton = textButton(self.__getButtonsFrame(), commandButton2)
        downloadButton.setText(textButton2, calculateFontSize(TEXT_SCALES["TextButton"], self.getAppController().getScreenSize()))
        downloadButton.setBackgroundColor(BUTTON_COLORS["Red"])
        downloadButton.setPadding(padx=50, pady=10)
        downloadButton.getInstance().grid(row=0, column=1, sticky="W", padx=25)

    def __getButtonsFrame(self):
        return self.__buttonsFrame


    def render(self):
        header = screenHeader(
            self, 
            lambda: self.switchScreen(self.getAppController().renderStartScreen()), 
            'Track Parameters',
            self.getAppController().getScreenSize()
        )

        # Create paramBoxGroup instance
        allParamBox = paramBoxGroup(self)

        # Create Buttons Frame
        self.__setButtonsFrame('Play Track', lambda: self.switchScreen(self.getAppController().renderParamsScreen()),
                               'Download', lambda: self.switchScreen(self.getAppController().renderLearnScreen()))
        
        # Grid configuration for the main frame
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Place header in the first row
        header.grid(row=0, column=0, sticky="NSEW", pady=20, columnspan=2)

        # Place ParamBoxGroup in the next rows
        allParamBox.grid(row=1, column=0, columnspan=2, sticky="NSEW", pady=20)

        # Place Buttons in the last row
        self.__getButtonsFrame().grid(row=5, column=0, sticky="N", columnspan=2)
        
        self.pack(expand=True, fill='both')
