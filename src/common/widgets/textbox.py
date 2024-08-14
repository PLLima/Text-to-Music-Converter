from common.classes import Child
from common.dictionaries import FONTS
from common.dictionaries import TEXTBOX_COLORS
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

class textbox(tk.Frame, Child):
    __allowedKeys = ('BackSpace', 'Delete', 'Down', 'Up', 'Left', 'Right', 'End', 'Home', 'KP_Up',
                            'KP_Down', 'KP_Left', 'KP_Right', 'KP_End', 'KP_Home')

    def __init__(self, parent, placeholder, maxCharacters, keyPressedFunction):
        tk.Frame.__init__(self, parent)
        self.setParent(parent)
        self.__setInstance()
        self.__setPlaceholder(placeholder)
        self.__setMaxCharacters(maxCharacters)
        self.__setForegroundColor(TEXTBOX_COLORS["Foreground"])
        self.__setKeyPressedFunction(keyPressedFunction)
        self.getInstance().bind('<FocusIn>', self.__focusIn)
        self.getInstance().bind('<FocusOut>', self.__focusOut)
        self.getInstance().bind('<KeyRelease>', lambda event: self.__checkCharacters(event))
        self.__writePlaceholder()
        self.__setScrollbar()
        self.getInstance().pack(expand=True, fill='both')

    def __setInstance(self):
        self.configure(bg=TEXTBOX_COLORS["Border"])
        self.configure(bd=0.5)
        self.__instance = tk.Text(self, borderwidth=0, highlightthickness= 0, relief='solid',
                                   bg=TEXTBOX_COLORS["Background"], wrap='word', padx=15, pady=15)

    def getInstance(self):
        return self.__instance

    def __setMaxCharacters(self, maxCharacters):
        self.__maxCharacters = maxCharacters
    
    def __getMaxCharacters(self):
        return self.__maxCharacters

    def getCharacterCount(self):
        return len(self.getContent())

    def __setPlaceholder(self, placeholder):
        self.__placeholder = placeholder

    def getPlaceholder(self):
        return self.__placeholder

    def __setKeyPressedFunction(self, keyPressedFunction):
        self.__keyPressedFunction = keyPressedFunction

    def __getKeyPressedFunction(self):
        return self.__keyPressedFunction

    def setHeight(self, heightInLines):
        self.__height = heightInLines
        self.getInstance().configure(height=heightInLines)

    def getHeight(self):
        return self.__height

    def setWidth(self, widthInCharacters):
        self.__width = widthInCharacters
        self.getInstance().configure(width=widthInCharacters)

    def getWidth(self):
        return self.__width

    def clearContent(self):
        self.getInstance().delete(1.0, 'end')

    def setContent(self, content):
        self.clearContent()
        self.getInstance().insert(1.0, content)

    def isEmpty(self):
        return self.getContent() == '\n'

    def getContent(self):
        return self.getInstance().get(1.0, tk.END)

    def __setFont(self, font):
        self.__font = font
        self.getInstance().configure(font=self.__font)

    def __getFont(self):
        return self.__font

    def setFontSize(self, fontSize):
        font = tkFont.Font(family=FONTS["Textbox"], size=fontSize)
        self.__setFont(font)

    def getFontSize(self):
        return self.__getFont().actual()["size"]

    def __setForegroundColor(self, foregroundColor):
        self.getInstance().configure(fg=foregroundColor)

    def __getForegroundColor(self):
        return self.getInstance().cget("fg")

    def __setScrollbar(self):
        self.__scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.getInstance().yview)
        self.getInstance().configure(yscrollcommand=self.__scrollbar.set)

    def __getScrollbar(self):
        return self.__scrollbar

    def __writePlaceholder(self):
        placeholder = self.getPlaceholder()
        if placeholder != None:
            self.setContent(placeholder)
            self.__setForegroundColor(TEXTBOX_COLORS["ForegroundPlaceholder"])

    def __isTextNotVisible(self):
        correctionTerm =  - 30
        contentHeight = self.getInstance().count("1.0", tk.END, "ypixels")[0]
        visibleHeight = self.getInstance().winfo_height() + correctionTerm
        return contentHeight > visibleHeight

    def __focusIn(self, *args):
        if self.__getForegroundColor() == TEXTBOX_COLORS["ForegroundPlaceholder"]:
            self.clearContent()
            self.__setForegroundColor(TEXTBOX_COLORS["Foreground"])

    def __focusOut(self, *args):
        if self.isEmpty():
            self.__writePlaceholder()

    def __checkCharacters(self, event, *args):
        # Execute external functions that depend on text input key presses
        keyPressedFunction = self.__getKeyPressedFunction()
        if keyPressedFunction != None:
            keyPressedFunction(event, *args)

        # Check if scrollbar should be created or not
        if self.__isTextNotVisible():
            self.getInstance().pack_forget()
            self.__getScrollbar().pack(side=tk.RIGHT, fill=tk.Y)
            self.getInstance().pack(expand=True, fill='both')
        else:
            self.__getScrollbar().pack_forget()

        if event.keysym in self.__allowedKeys:
            return

        if self.getCharacterCount() > self.__getMaxCharacters():
            self.getInstance().delete('1.0 + %d chars' % self.__getMaxCharacters(), tk.END)
            return 'break'

    def enable(self):
        self.getInstance().configure(state=tk.NORMAL)
        self.__setForegroundColor(TEXTBOX_COLORS["Foreground"])

    def disable(self):
        self.getInstance().tag_configure("disabled", foreground=TEXTBOX_COLORS["ForegroundDisabled"])
        self.getInstance().tag_configure("sel", foreground=TEXTBOX_COLORS["ForegroundDisabled"])
        self.getInstance().tag_add("disabled", "1.0", tk.END)
        # Check if scrollbar should be created or not
        if self.__isTextNotVisible():
            self.getInstance().pack_forget()
            self.__getScrollbar().pack(side=tk.RIGHT, fill=tk.Y)
            self.getInstance().pack(expand=True, fill='both')
        self.getInstance().configure(state=tk.DISABLED)