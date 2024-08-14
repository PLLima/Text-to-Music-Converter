import tkinter as tk
from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES, FONTS

class tableCell(tk.Frame):
    def __init__(self, parent, text, font, bg, fg, wraplength, padding, bold=False):
        super().__init__(parent, bd=0.5, bg='#636363')
        self.label = tk.Label(self, text=text, font=font, fg=fg, bg=bg, 
                              wraplength=wraplength, justify='center', anchor='center')
        if bold:
            self.label.configure(font=(font[0], font[1], 'bold'))
        self.label.pack(expand=True, fill='both', ipadx=padding, ipady=padding)

class table:
    def __init__(self, parent, screenSize):
        # Table data
        self.data = [
            ('Text', 'Musical Action or Instrument', 'Text', 'Musical Action or Instrument'),
            ('A or a', 'Note A', '-', 'Reset volume to initial set value'),
            ('B or b', 'Note B', 'O, o, U, u, I or i', 'Repeat last note or play MIDI instrument "Telephone Ring" (125)'),
            ('C or c', 'Note C', 'R+', 'Increase one octave'),
            ('D or d', 'Note D', 'R-', 'Decrease one octave'),
            ('E or e', 'Note E', '?', 'Plays a random note'),
            ('F or f', 'Note F', 'NL (New Line)', 'Change MIDI instrument randomly (between 1 and 128)'),
            ('G or g', 'Note G', 'BPM+', 'Increase BPM by 80'),
            ('Space', 'Silence or pause', ';', 'Change BPM to random value'),
            ('+', 'Double the volume', 'Any other Character', 'Keep previous state')
        ]
        self.screenSize = screenSize
        self.minCellWidth = 155
        self.padding = 7
        
        self.createTable(parent)

    def createTable(self, parent):
        self.tableFrame = tk.Frame(parent, bd=0.5, bg='#636363')

        for i, row in enumerate(self.data):
            for j, cell_text in enumerate(row):
                cell_font = (FONTS["Table"], calculateFontSize(TEXT_SCALES["TableContent"], self.screenSize), 'normal')
                cell_bg = '#ffffff'
                cell_fg = '#636363'
                wraplength = self.minCellWidth
                bold = (i == 0)
                
                if bold:
                    cell_bg = '#dcdcdc'
                
                cell = tableCell(self.tableFrame, text=cell_text, font=cell_font, bg=cell_bg, fg=cell_fg, 
                                 wraplength=wraplength, padding=self.padding, bold=bold)
                cell.grid(row=i, column=j, padx=0, pady=0, sticky='nsew')

        self.configureLayout(parent)
        self.tableFrame.pack()

    def configureLayout(self, parent):
        totalColumns = len(self.data[0])
        totalRows = len(self.data)

        # Adjust columns to have the same minimum width
        for j in range(totalColumns):
            parent.grid_columnconfigure(j, weight=1, minsize=self.minCellWidth)

        # Adjust rows to have the same height
        for i in range(totalRows):
            parent.grid_rowconfigure(i, weight=1)
