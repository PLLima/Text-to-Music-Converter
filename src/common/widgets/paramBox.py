import tkinter as tk
from common.functions import calculateFontSize
from common.dictionaries import SCREEN_COLORS, TEXT_SCALES, FONTS
from common.classes import Child
import tkinter.font as tkFont


class paramBox(tk.Frame):
    def __init__(self, parent, line1="", line2="", width=200, height=200, font_family="Arial", font_size=12, font_weight="normal", font_color="#000000", bg='#d9d9d9', border_color="#636363", border_width=2):
        super().__init__(parent, bg=SCREEN_COLORS["Background"], width=width, height=height)
        self.line1 = line1
        self.line2 = line2
        self.width = width
        self.height = height
        self.font_family = font_family
        self.font_size = font_size
        self.font_weight = font_weight
        self.font_color = font_color
        self.bg = bg
        self.border_color = border_color
        self.border_width = border_width
        self.setInstance()

    def setInstance(self):
        self.font = tkFont.Font(family=self.font_family, size=self.font_size, weight=self.font_weight)
        self.label = tk.Label(self, text=f"{self.line1}\n{self.line2}", font=self.font, bg=self.bg, fg=self.font_color, anchor='center', justify='center', padx=10, pady=10, borderwidth=self.border_width, relief='solid', highlightbackground=self.border_color)
        self.label.place(x=0, y=0, width=self.width, height=self.height)

    def setContent(self, line1, line2):
        self.line1 = line1
        self.line2 = line2
        self.label.config(text=f"{self.line1}\n{self.line2}")

    def setFont(self, font_family=None, font_size=None, font_weight=None, font_color=None):
        if font_family:
            self.font_family = font_family
        if font_size:
            self.font_size = font_size
        if font_weight:
            self.font_weight = font_weight
        if font_color:
            self.font_color = font_color
        self.font.config(family=self.font_family, size=self.font_size, weight=self.font_weight)
        self.label.config(font=self.font, fg=self.font_color)

    def setDimensions(self, width, height):
        self.width = width
        self.height = height
        self.config(width=self.width, height=self.height)
        self.label.place_configure(width=self.width, height=self.height)

    def setBorder(self, border_color=None, border_width=None):
        if border_color:
            self.border_color = border_color
        if border_width is not None:
            self.border_width = border_width
        self.label.config(borderwidth=self.border_width, highlightbackground=self.border_color)

    def getContent(self):
        return self.line1, self.line2

    def getFont(self):
        return {
            "family": self.font_family,
            "size": self.font_size,
            "weight": self.font_weight,
            "color": self.font_color
        }

    def getDimensions(self):
        return self.width, self.height

    def getBorder(self):
        return {
            "color": self.border_color,
            "width": self.border_width
        }

