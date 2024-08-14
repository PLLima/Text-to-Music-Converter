import tkinter as tk

from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES
from common.dictionaries import FONTS

class table():
    def __init__(self, parent, screenSize):
        # Table data
        lst = [('Text', 'Musical Action or Instrument', 'Text', 'Musical Action or Instrument'),
               ('A or a', 'Note A', '-', 'Reset volume to initial set value'),
               ('B or b', 'Note B', 'O, o, U, u, I or i', 'If last character was a note then repeat it, else play MIDI instrument "Telephone Ring"(125)'),
               ('C or c', 'Note C', 'R+', 'Increase one octave'),
               ('D or d', 'Note D', 'R-', 'Decrease one octave'),
               ('E or e', 'Note E', '?', 'Plays a random note'),
               ('F or f', 'Note F', 'NL (New Line)', 'Change MIDI instrument randomly (between 1 and 128)'),
               ('G or g', 'Note G', 'BPM+', 'Increase BPM by 80'),
               ('Space', 'Silence or pause', ';', 'Change BPM to random value'),
               ('+', 'Double the volume', 'Any other Character', 'Keep previous state')]
        
        total_rows = len(lst)
        total_columns = len(lst[0])

        border_thickness = 0.5
        min_cell_width = 155
        # Internal Label paddings
        iPadding = 7

        self.tableFrame = tk.Frame(parent, bd=border_thickness, bg='#636363')

        # Create table using bordered Labels
        for i in range(total_rows):
            for j in range(total_columns):
                # Define an apropriate value for cell width
                wraplength = min_cell_width
                self.eFrame = tk.Frame(self.tableFrame, bd=border_thickness, bg='#636363')
                self.e = tk.Label(self.eFrame, fg='#636363', font=(FONTS["Table"], calculateFontSize(TEXT_SCALES["TableContent"], screenSize), 'normal'), 
                                   text=lst[i][j], anchor='center', wraplength=wraplength, justify='center', background='#ffffff')
                if i == 0:
                    self.e.configure(font=(FONTS["Table"], calculateFontSize(TEXT_SCALES["TableContent"], screenSize), 'bold'))
                    self.e.configure(background='#dcdcdc')
                self.e.pack(expand=True, fill='both', ipadx=iPadding, ipady=iPadding)
                self.eFrame.grid(row=i, column=j, padx=0, pady=0, sticky='nsew')

        # Adjust columns to have the same minimum width
        for j in range(total_columns):
            parent.grid_columnconfigure(j, weight=1, minsize=min_cell_width)
        # Adjust lines to have the same height
        for i in range(total_rows):
            parent.grid_rowconfigure(i, weight=1)

        self.tableFrame.pack()