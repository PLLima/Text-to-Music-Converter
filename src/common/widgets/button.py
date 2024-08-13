from common.classes import Child
from common.dictionaries import FONTS
from common.dictionaries import SCREEN_COLORS, BUTTON_COLORS, BUTTON_ICONS
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

class button(tk.Frame, Child):
    def __init__(self, parent, clickHandler):
        self.setParent(parent)
        tk.Frame.__init__(self, self.getParent(), bg=SCREEN_COLORS["Background"])
        self.__setEventHandler(clickHandler)
        self.__setInstance()

    def __setInstance(self):
        self.__instance = tk.Button(self.getParent(), command=self.getEventHandler(),
                                    highlightbackground=SCREEN_COLORS["Background"], bg=SCREEN_COLORS["Background"], bd=0)

    def getInstance(self):
        return self.__instance

    def __setEventHandler(self, eventHandler):
        self.__eventHandler = eventHandler

    def getEventHandler(self):
        return self.__eventHandler

    def setPadding(self, padx, pady):
        self.getInstance().configure(padx=padx, pady=pady)

    def getPaddingX(self):
        return self.getInstance().cget("padx")

    def getPaddingY(self):
        return self.getInstance().cget("pady")

class textButton(button):
    def __init__(self, parent, clickHandler):
        super().__init__(parent, clickHandler)
        self.getInstance().configure(fg=BUTTON_COLORS["Foreground"])
        self.getInstance().configure(disabledforeground=BUTTON_COLORS["Foreground"])
        self.getInstance().configure(activeforeground=BUTTON_COLORS["Foreground"])
        self.getInstance().configure(highlightcolor=BUTTON_COLORS["Foreground"])
        self.getInstance().configure(cursor='hand2')

    def __setFont(self, fontSize):
        self.__font = tkFont.Font(family=FONTS["TextButton"], size=fontSize)
        self.getInstance().configure(font=self.__font)

    def setText(self, text, fontSize):
        self.__setFont(fontSize)
        self.getInstance().configure(text=text)

    def getText(self):
        return self.getInstance().cget("text");

    def __setBackgroundColorRed(self):
        self.getInstance().configure(bg=BUTTON_COLORS["Red"])
        self.getInstance().configure(activebackground=BUTTON_COLORS["RedActive"])
        self.getInstance().configure(highlightbackground=BUTTON_COLORS["RedActive"])

    def __setBackgroundColorBlack(self):
        self.getInstance().configure(bg=BUTTON_COLORS["Black"])
        self.getInstance().configure(activebackground=BUTTON_COLORS["BlackActive"])
        self.getInstance().configure(highlightbackground=BUTTON_COLORS["BlackActive"])

    def __setBackgroundColorGray(self):
        self.getInstance().configure(bg=BUTTON_COLORS["Gray"])
        self.getInstance().configure(activebackground=BUTTON_COLORS["Gray"])
        self.getInstance().configure(highlightbackground=BUTTON_COLORS["Gray"])
        self.getInstance().configure(cursor='X_cursor')

    def setBackgroundColor(self, backgroundColor):
        if backgroundColor == BUTTON_COLORS["Red"]:
            self.__setBackgroundColorRed()
        elif backgroundColor == BUTTON_COLORS["Black"]:
            self.__setBackgroundColorBlack()
        elif backgroundColor == BUTTON_COLORS["Gray"]:
            self.__setBackgroundColorGray()

    def getBackgroundColor(self):
        return self.getInstance().cget("bg")

    def enable(self):
        self.getInstance().configure(state=tk.NORMAL)

    def disable(self):
        self.setBackgroundColor(BUTTON_COLORS["Gray"])
        self.getInstance().configure(state=tk.DISABLED)

class iconButton(button):
    def __init__(self, parent, clickHandler):
        super().__init__(parent, clickHandler)
        self.getInstance().configure(highlightcolor=BUTTON_COLORS["Foreground"])
        self.getInstance().configure(cursor='hand2')

    def setIcon(self, image):
        self.__icon = image
        self.getInstance().configure(image=image)

    def getIcon(self):
        return self.__icon
    
class backButton(iconButton):
    def __init__(self, parent, clickHandler):
        super().__init__(parent, clickHandler)
        
        backarrow = Image.open(BUTTON_ICONS["BackArrow"])
        icon = ImageTk.PhotoImage(backarrow.resize((56,56)))
        self.setIcon(icon)