import tkinter as tk
import tkinter.font as tkFont

class paramBox(tk.Frame):
    def __init__(self, parent, line1="", line2="", width=200, height=200, fontFamily="Arial", fontSize=12, fontColor="#000000", bg='#d9d9d9', borderColor="#636363", borderWidth=2):
        super().__init__(parent, bg=bg, width=width, height=height, bd=0, highlightthickness=0)
        self.line1 = line1
        self.line2 = line2
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.bg = bg
        self.borderColor = borderColor
        self.borderWidth = borderWidth
        self.setInstance()

    def setInstance(self):
        # Configure frame's border
        self.configure(bd=self.borderWidth, bg=self.borderColor)

        # Creates an internal frame to fill background correctly
        self.inner_frame = tk.Frame(self, bg=self.bg)
        self.inner_frame.grid_columnconfigure(0, weight=1)
        self.inner_frame.grid_rowconfigure((0, 1), weight=1)

        # Configures fonts for both lines
        self.font_line1 = tkFont.Font(family=self.fontFamily, size=self.fontSize, weight="bold")
        self.font_line2 = tkFont.Font(family=self.fontFamily, size=self.fontSize, weight="normal")

        # Creates labels for each line
        self.label_line1 = tk.Label(self.inner_frame, text=self.line1, font=self.font_line1, bg=self.bg, fg=self.fontColor)
        self.label_line2 = tk.Label(self.inner_frame, text=self.line2, font=self.font_line2, bg=self.bg, fg=self.fontColor)

        # Places them inside the inner label
        self.label_line1.grid(row=0, column=0, sticky="S")
        self.label_line2.grid(row=1, column=0, sticky="N")
        self.inner_frame.pack(expand=True, fill='both')

    def setContent(self, line1, line2):
        self.line1 = line1
        self.line2 = line2
        self.label_line1.config(text=self.line1)
        self.label_line2.config(text=self.line2)

    def setFont(self, fontFamily=None, fontSize=None, fontColor=None):
        if fontFamily:
            self.fontFamily = fontFamily
        if fontSize:
            self.fontSize = fontSize
        if fontColor:
            self.fontColor = fontColor

        self.font_line1.config(family=self.fontFamily, size=self.fontSize, weight="bold")
        self.font_line2.config(family=self.fontFamily, size=self.fontSize, weight="normal")
        self.label_line1.config(font=self.font_line1, fg=self.fontColor)
        self.label_line2.config(font=self.font_line2, fg=self.fontColor)

    def setDimensions(self, width, height):
        self.config(width=width, height=height)
        self.inner_frame.config(width=width, height=height)

    def setBorder(self, borderColor=None, borderWidth=None):
        if borderColor:
            self.borderColor = borderColor
        if borderWidth is not None:
            self.borderWidth = borderWidth
        self.configure(borderwidth=self.borderWidth, relief='solid', highlightbackground=self.borderColor)

    def getContent(self):
        return self.line1, self.line2

    def getFont(self):
        return {
            "family": self.fontFamily,
            "size": self.fontSize,
            "color": self.fontColor
        }

    def getDimensions(self):
        return self.winfo_width(), self.winfo_height()

    def getBorder(self):
        return {
            "color": self.borderColor,
            "width": self.borderWidth
        }
