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
from trackControl.player import player
import math

class playerScreen(tk.Frame, Screen):
    def __init__(self, appController, initialVolume, initialBpm, initialOctave, initialString, midiFile):
        self.setParent(appController.getParent())
        tk.Frame.__init__(self, self.getParent(), bg=SCREEN_COLORS["Background"])
        self.setAppController(appController)


        # Store initial values
        self.initialVolume = initialVolume 
        self.initialBpm = initialBpm 
        self.initialOctave = initialOctave
        self.initialString = initialString
        self.controlAfter = None


        self.controlPause = 0

        # Initialize UI elements
        self.playTrackButton = None
        self.downloadResetButton = None
        self.slider = None


        self.setMusic(midiFile)
        self.getParent().protocol("WM_DELETE_WINDOW", self.onWindowClosing)
        self.loadMusicStart()
        self.render()

    def getMusic(self):
        return self.music

    def setMusic(self, midiFile):
        self.music = player(midiFile)

    def getMusicTotalTime(self):
        return self.getMusic().getMusicLength()
    
    def getMusicActualTime(self):
        return self.getMusic().getTime()

    def loadMusicStart(self):
        self.getMusic().loadMusic()

        

    def createButtons(self, textButton1, commandButton1, textButton2, commandButton2):
        buttonsFrame = tk.Frame(self, bg=SCREEN_COLORS["Background"])

        buttonsFrame.grid_rowconfigure(0, weight=1)
        buttonsFrame.grid_columnconfigure((0, 1), weight=1)

        self.playTrackButton = self.createButton(
            buttonsFrame, textButton1, commandButton1, column=0, sticky="E", padx=25, pad=(45, 10)
        )

        self.downloadResetButton = self.createButton(
            buttonsFrame, textButton2, commandButton2, column=1, sticky="W", padx=25, pad=(50, 10)
        )

        return buttonsFrame

    def createButton(self, parent, text, command, column, sticky, padx, pad):
        button = textButton(parent, command)
        button.setText(text, calculateFontSize(TEXT_SCALES["TextButton"], self.getAppController().getScreenSize()))
        button.setBackgroundColor(BUTTON_COLORS["Red"])
        button.setPadding(padx=pad[0], pady=pad[1])
        button.getInstance().grid(row=0, column=column, sticky=sticky, padx=padx)
        return button

    def onSliderChange(self, value):
        print(f"Slider changed to: {value}")


    def updateSliderPerSec(self):
        currentValue = self.slider.getValue()

        if currentValue < self.getMusicTotalTime():
            self.slider.setValue(currentValue + 1)
        self.controlAfter = self.after(1000, self.updateSliderPerSec)

    def pauseAfter(self):
        if self.controlAfter is not None:
            self.after_cancel(self.controlAfter)
            controlAfter = None

    def pressPlay(self):
        currentTextPT = self.playTrackButton.getText()  # Get the current text of the play track button
        if currentTextPT == "Play Track":
            if self.controlPause == 0:
                self.getMusic().playMusic()
                self.updateSliderPerSec()
                self.controlPause = 1
            else:
                self.getMusic().unpauseMusic()  
                self.updateSliderPerSec()
            newTextPT = "Pause Track"
            newTextDR = "Reset"  # Change button to Reset
        else:
            self.getMusic().pauseMusic()
            self.pauseAfter()
            newTextPT = "Play Track"
            newTextDR = "Download"  # Change button to Download

        # Update button texts and widths
        self.updateButton(self.playTrackButton, newTextPT)
        self.updateButton(self.downloadResetButton, newTextDR)

    def updateButton(self, button, text):
        button.setText(text, calculateFontSize(TEXT_SCALES["TextButton"], self.getAppController().getScreenSize()))
        button.getInstance().config(width=12)

    def pressDownloadReset(self):
        if self.downloadResetButton.getText() == "Download":
            self.download()
        else:
            self.reset()

    def download(self):
        self.getMusic().downloadMusic()

    def reset(self):
        self.getMusic().playMusic()

    def returnScreen(self):
        self.getMusic().pauseMusic()
        self.getMusic().unloadMusic()
        self.switchScreen(self.getAppController().renderParamsScreen())

    def onWindowClosing(self):
        
        self.getMusic().unloadMusic()
        self.getParent().destroy()

    def render(self):
        # Create header
        header = screenHeader(
            self, 
            self.returnScreen, 
            'Track Parameters',
            self.getAppController().getScreenSize()
        )

        print(self.getMusicTotalTime())
        musicTime = math.ceil(self.getMusicTotalTime())
        # Create slider
        self.slider = sliderWithLabel(
            parent=self,
            minValue=0,
            maxValue=musicTime,
            length=600,
            command=lambda: self.on_slider_change,
            initialValue=0
        )
        print(musicTime)

        #self.slider.disable()

        # Create textbox for string input
        stringInput = textbox(
            parent=self,
            placeholder=None,
            maxCharacters=TEXTBOX_PARAMS["MaxCharacters"],
            keyPressedFunction=None
        )
        stringInput.setContent(self.initialString)
        stringInput.disable()

        # Create paramBoxGroup
        allParamBox = paramBoxGroup(
            self, 
            volume=f"{self.initialVolume}%", 
            bpm=self.initialBpm, 
            octave=self.initialOctave
        )

        # Create buttons frame
        buttonsFrame = self.createButtons('Play Track', self.pressPlay, 'Download', self.pressDownloadReset)

        # Configure grid layout
        self.grid_rowconfigure((0, 1, 2, 3), weight=1, minsize=80)
        self.grid_columnconfigure((0, 1), weight=1)

        # Position widgets in the grid
        header.grid(row=0, column=0, sticky="NSEW", pady=20, columnspan=2)
        allParamBox.grid(row=1, column=0, sticky="NSEW", pady=20)
        stringInput.grid(row=1, column=1, sticky="NSEW", pady=20, padx=(0, 95))
        self.slider.grid(row=2, column=0, sticky="N", columnspan=2, pady=(20, 0))
        buttonsFrame.grid(row=3, column=0, sticky="N", columnspan=2)

        self.pack(expand=True, fill='both')
