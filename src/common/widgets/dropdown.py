import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from common.classes import Child
from common.dictionaries import SCREEN_COLORS, SLIDER_COLORS, FONTS, FONT_SIZES

class titledDropdown(tk.Frame, Child):
    def __init__(self, parent, initialValue, *options):
        self.setParent(parent)
        tk.Frame.__init__(self, self.getParent(), bg=SCREEN_COLORS["Background"])
        self.setTitleText('', 1)
        self.__createOptionMenu(self, initialValue, *options)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

    def setTextPadding(self, padx):
        self.__padx = padx
        self.__getTitle().grid(row=0, column=0, sticky="E", padx=(0, self.getTextPadding()))

    def getTextPadding(self):
        return self.__padx
    
    def __setTitle(self, title, fontSize):
        titleFont = tkFont.Font(family=FONTS["Dropdown"], size=fontSize, weight='bold')
        self.__title = tk.Label(self, text=title, font=titleFont, bg=SCREEN_COLORS["Background"], fg=SLIDER_COLORS["Foreground"])

    def __getTitle(self):
        return self.__title

    def setTitleText(self, text, fontSize):
        self.__titleText = text
        self.__setTitle(text, fontSize)

    def getTitleText(self):
        return self.__titleText

    def __getSelectedVariable(self):
        return self.__selectedVariable

    def __createOptionMenu(self, parent, initialValue, *options):
        self.__selectedVariable = tk.StringVar()
        self.__getSelectedVariable().set(initialValue)
        optionMenu = tk.OptionMenu(parent, self.__getSelectedVariable(), *options, command=self.__onSelectedOption)
        optionMenu.grid(row=0, column=1, sticky="E")

    def getSelectedValue(self):
        return self.__getSelectedVariable().get()
    
    def __onSelectedOption(self, *args):
        pass