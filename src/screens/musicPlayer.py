import tkinter as tk
from tkinter import ttk
from common.functions import calculateFontSize
from common.dictionaries import SCREEN_COLORS, TEXT_SCALES, BUTTON_COLORS, FONTS
from common.widgets.button import textButton
from common.classes import Screen
from common.widgets.screenHeader import screenHeader
from common.widgets.paramBoxGroup import paramBoxGroup
from common.widgets.sliderWithLabel import sliderWithLabel

class playerScreen(tk.Frame, Screen):
    def __init__(self, appController):
        self.setParent(appController.getParent())
        tk.Frame.__init__(self, self.getParent(), bg=SCREEN_COLORS["Background"])
        self.setAppController(appController)

    def __setButtonsFrame(self, textButton1, commandButton1, textButton2, commandButton2):
        self.__buttonsFrame = tk.Frame(self, bg=SCREEN_COLORS["Background"])

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

    def on_slider_change(self, value):
        print(f"Slider changed to: {value}")

    def render(self):
        header = screenHeader(
            self, 
            lambda: self.switchScreen(self.getAppController().renderStartScreen()), 
            'Track Parameters',
            self.getAppController().getScreenSize()
        )

        slider = sliderWithLabel(
            parent=self,
            from_=0,
            to=100,
            length=600,
            command=self.on_slider_change,
            initial_value=50
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

        # Place Slider at 4th row
        slider.grid(row=4, column=0, sticky="N", columnspan=2)

        # Place Buttons in the last row
        self.__getButtonsFrame().grid(row=5, column=0, sticky="N", columnspan=2)
        
        self.pack(expand=True, fill='both')
