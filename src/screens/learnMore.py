import tkinter as tk
from tkinter import ttk

from common.classes import Screen
from common.widgets.screenHeader import screenHeader
from common.widgets.table import table

class learnScreen(ttk.Frame, Screen):
    def __init__(self, appController):
        self.setParent(appController.getParent())
        ttk.Frame.__init__(self, self.getParent())
        self.setAppController(appController)

    def render(self):
        header = screenHeader(self, lambda: self.switchScreen(self.getAppController().renderStartScreen()), 'Character Mapping',
                              self.getAppController().getScreenSize())
        titleFrame = ttk.Frame(header)
        tableFrame = ttk.Frame(self)
        # Center widgets inside main frame
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Add table widget to tableFrame
        table(tableFrame, self.getAppController().getScreenSize())

        header.grid(row=0, column=0, sticky="NSEW", pady=20)
        titleFrame.grid(row=0, column=1, sticky="")
        tableFrame.grid(row=1, column=0, sticky="N")
        self.pack(expand=True, fill='both')