from tkinter import ttk

from common.classes import Child, Closeable
from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES, BUTTON_COLORS
from common.widgets.title import mainHeader, mainSubtitle
from common.widgets.button import textButton
from screens.learnMore import learnScreen

class startScreen(ttk.Frame, Child, Closeable):
    def __init__(self, parent, screenSize):
        ttk.Frame.__init__(self, parent)
        self.setParent(parent)
        self.screenSize = screenSize

    def switchScreen(self, nextScreen):
        # Destroy the current screen and render the next one.
        self.destroyCurrentScreen()
        nextScreen.render()

    def destroyCurrentScreen(self):
        # Destroy the current frame and its widgets.
        if self.currentFrame:
            self.currentFrame.destroy()

    def createMainFrame(self):
        # Create and configure the main frame and its widgets.
        frame = ttk.Frame(self.getParent())
        frame.pack(expand=True, fill='both')

        textsFrame = ttk.Frame(frame)
        buttonsFrame = ttk.Frame(frame)

        # Centraliza os widgets dentro do frame
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        title = mainHeader(textsFrame)
        title.setFontSize(calculateFontSize(TEXT_SCALES["MainHeader"], self.screenSize))
        title.setContent('Turn Text into Music')
        title.getInstance().pack(pady=25)

        subtitle = mainSubtitle(textsFrame)
        subtitle.setFontSize(calculateFontSize(TEXT_SCALES["MainSubtitle"], self.screenSize))
        subtitle.setContent('Create beautiful melodies from your words')
        subtitle.getInstance().pack(pady=[0, 90])

        buttonsFrame.grid_rowconfigure(0, weight=1)
        buttonsFrame.grid_columnconfigure(0, weight=1)
        buttonsFrame.grid_columnconfigure(1, weight=1)

        getStartedButton = textButton(buttonsFrame, None)
        getStartedButton.setText('Get Started', calculateFontSize(TEXT_SCALES["TextButton"], self.screenSize))
        getStartedButton.setBackgroundColor(BUTTON_COLORS["Red"])
        getStartedButton.setPadding(padx=45, pady=10)
        getStartedButton.getInstance().grid(row=0, column=0, sticky="E", padx=25)

        learnMoreButton = textButton(buttonsFrame, lambda: self.switchScreen(learnScreen(self.getParent(), self.screenSize)))
        learnMoreButton.setText('Learn More', calculateFontSize(TEXT_SCALES["TextButton"], self.screenSize))
        learnMoreButton.setBackgroundColor(BUTTON_COLORS["Black"])
        learnMoreButton.setPadding(padx=50, pady=10)
        learnMoreButton.getInstance().grid(row=0, column=1, sticky="W", padx=25)

        textsFrame.grid(row=0, column=0, sticky="S")
        buttonsFrame.grid(row=1, column=0, sticky="N")

        return frame

    def render(self):
        self.currentFrame = self.createMainFrame()
