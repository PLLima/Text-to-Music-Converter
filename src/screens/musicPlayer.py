import tkinter as tk
from tkinter import ttk
from common.functions import calculateFontSize
from common.dictionaries import SCREEN_COLORS, TEXT_SCALES, BUTTON_COLORS, FONTS, TEXTBOX_PARAMS
from common.widgets.button import textButton
from common.classes import Screen
from common.widgets.screenHeader import screenHeader
from common.widgets.paramBoxGroup import paramBoxGroup
from common.widgets.slider import sliderWithLabel
from common.widgets.textbox import textbox
from trackControl import player

class playerScreen(tk.Frame, Screen):
    def __init__(self, appController, initialVolume, initialBpm, initialOctave, initialString):
        self.setParent(appController.getParent())
        tk.Frame.__init__(self, self.getParent(), bg=SCREEN_COLORS["Background"])
        self.setAppController(appController)
        self.playTrackButton = None  # Initialize the play track button attribute
        self.downloadResetButton = None   # Initialize the download button attribute
        self.slider = None           # Initialize the slider attribute
        
        self.initialVolume = initialVolume 
        self.initialBpm = initialBpm 
        self.initialOctave = initialOctave
        self.initialString = initialString

        self.controlPause = 0

        self.loadMusicStart()

    def loadMusicStart(self):
        # ADICIONAR AQUI O LOAD DA MUSICA
        # music = player.setPlayer(midiFile)
        # music.loadMusic()
        pass

    def __setButtonsFrame(self, textButton1, commandButton1, textButton2, commandButton2):
        self.__buttonsFrame = tk.Frame(self, bg=SCREEN_COLORS["Background"])

        self.__getButtonsFrame().grid_rowconfigure(0, weight=1)
        self.__getButtonsFrame().grid_columnconfigure((0, 1), weight=1)

        self.playTrackButton = textButton(self.__getButtonsFrame(), commandButton1)  # Store the play track button reference
        self.playTrackButton.setText(textButton1, calculateFontSize(TEXT_SCALES["TextButton"], self.getAppController().getScreenSize()))
        self.playTrackButton.setBackgroundColor(BUTTON_COLORS["Red"])
        self.playTrackButton.setPadding(padx=45, pady=10)
        self.playTrackButton.getInstance().grid(row=0, column=0, sticky="E", padx=25)

        self.downloadResetButton = textButton(self.__getButtonsFrame(), commandButton2)  # Store the download button reference
        self.downloadResetButton.setText(textButton2, calculateFontSize(TEXT_SCALES["TextButton"], self.getAppController().getScreenSize()))
        self.downloadResetButton.setBackgroundColor(BUTTON_COLORS["Red"])
        self.downloadResetButton.setPadding(padx=50, pady=10)
        self.downloadResetButton.getInstance().grid(row=0, column=1, sticky="W", padx=25)

    def __getButtonsFrame(self):
        return self.__buttonsFrame

    def on_slider_change(self, value):
        print(f"Slider changed to: {value}")

    def pressPlay(self):
        if self.playTrackButton:  # Check if the play track button is initialized
            current_textPT = self.playTrackButton.getText()  # Get the current text of the play track button
            if current_textPT == "Play Track":
                if self.controlPause == 0:
                    player.playMusic()
                    self.controlPause = 1
                else:
                    player.unpauseMusic()  
                new_textPT = "Pause Track"
                new_textDR = "Reset" # Change button to Reset
            else:
                player.pauseMusic()
                new_textPT = "Play Track"
                new_textDR = "Download" # Change button to Download
            # Set the new text for the play track button
            self.playTrackButton.setText(new_textPT, calculateFontSize(TEXT_SCALES["TextButton"], self.getAppController().getScreenSize()))
            self.playTrackButton.getInstance().config(width=12) # Set a fixed width for the button to prevent resizing
            if self.downloadResetButton:
                self.downloadResetButton.getInstance().config(width=12) # Set a fixed width for the button to prevent resizing
                self.downloadResetButton.setText(new_textDR, calculateFontSize(TEXT_SCALES["TextButton"], self.getAppController().getScreenSize()))

    def pressDownloadReset(self):
        currentDR_text = self.downloadResetButton.getText()  # Get the current text of the Download/Reset track button
        if currentDR_text == "Download": #Call Reset/Download based on button state
            self.download()
        else:
            self.reset()
        
    def download():
        pass

    def reset():
        pass

    def render(self):
        header = screenHeader(
            self, 
            lambda: self.switchScreen(self.getAppController().renderStartScreen()), 
            'Track Parameters',
            self.getAppController().getScreenSize()
        )

        self.slider = sliderWithLabel(
            parent=self,
            from_=0,
            to=100,
            length=600,
            command=self.on_slider_change,
            initial_value=0
        )

        # Disable the slider
        if self.slider:
            self.slider.slider.config(state=tk.DISABLED)

        stringInput = textbox(
            parent=self,
            placeholder=None,
            maxCharacters=TEXTBOX_PARAMS["MaxCharacters"],
            keyPressedFunction=None
        )


        stringInput.setContent(self.initialString)
        stringInput.disable()

        # Create paramBoxGroup instance
        allParamBox = paramBoxGroup(
            self, 
            volume = f"{self.initialVolume}%", 
            bpm = self.initialBpm, 
            octave = self.initialOctave
            )

        # Create Buttons Frame
        self.__setButtonsFrame('Play Track', lambda: self.pressPlay(),
                               'Download', lambda: self.pressDownloadReset())
        
        # Grid configuration for the main frame
        self.grid_rowconfigure((0, 1, 2, 3), weight=1, minsize=80)
        self.grid_columnconfigure((0, 1), weight=1)

        # Place header in the first row
        header.grid(row=0, column=0, sticky="NSEW", pady=20, columnspan=2)

        # Place ParamBoxGroup in the next rows
        allParamBox.grid(row=1, column=0, columnspan=1, sticky="NSEW", pady=20)

        # Place StringInput Textbox in the next rows
        stringInput.grid(row=1, column=1, columnspan=1, sticky="NSEW", pady=20, padx=(0, 95))

        # Place Slider at 2th row
        self.slider.grid(row=2, column=0, sticky="N", columnspan=2, pady=(20, 0))

        # Place Buttons in the last row
        self.__getButtonsFrame().grid(row=3, column=0, sticky="N", columnspan=2)
        
        self.pack(expand=True, fill='both')
