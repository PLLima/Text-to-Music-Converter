import tkinter as tk
from tkinter import ttk

from common.classes import Screen
from common.widgets.screenHeader import screenHeader

class playerScreen(ttk.Frame, Screen):
    def __init__(self, appController):
        self.setParent(appController.getParent())
        ttk.Frame.__init__(self, self.getParent())
        self.setAppController(appController)

    def render(self):
        header = screenHeader(self, lambda: self.switchScreen(self.getAppController().renderStartScreen()), 'Track Parameters',
                              self.getAppController().getScreenSize())
        titleFrame = ttk.Frame(header)
        tableFrame = ttk.Frame(self)
        # Center widgets inside main frame
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        

        header.grid(row=0, column=0, sticky="NSEW", pady=20, columnspan=2)
        
 
        self.pack(expand=True, fill='both')