from tkinter import ttk

from common.classes import Screen
from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES, BUTTON_COLORS
from common.widgets.screenHeader import screenHeader
from common.widgets.button import textButton

class paramsScreen(ttk.Frame, Screen):
    def __init__(self, appController):
        self.setParent(appController.getParent())
        ttk.Frame.__init__(self, self.getParent())
        self.setAppController(appController)

    def render(self):
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = screenHeader(self, lambda: self.switchScreen(self.getAppController().renderStartScreen()), 'Initial Parameters',
                              self.getAppController().getScreenSize())

        header.grid(row=0, column=0, sticky="NSEW", pady=20)
        self.pack(expand=True, fill='both')