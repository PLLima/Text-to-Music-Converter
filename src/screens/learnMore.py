from common.classes import Child
from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES
from common.dictionaries import FONTS
from common.widgets.title import screenTitle
import tkinter as tk
from tkinter import ttk

class Table():
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
        min_cell_width = 150
        # Internal Label paddings
        iPadding = 7

        # Create table using bordered Labels
        for i in range(total_rows):
            for j in range(total_columns):
                # Define an apropriate value for cell width
                wraplength = min_cell_width
                if i == 0:
                    self.e = tk.Label(parent, fg='#636363', font=(FONTS["Table"], calculateFontSize(TEXT_SCALES["TableContent"], screenSize), 'bold'), 
                                   text=lst[i][j], borderwidth=border_thickness, relief='solid', anchor='center',
                                   wraplength=wraplength, justify='center', background='#dcdcdc')
                else:
                    self.e = tk.Label(parent, fg='#636363', font=(FONTS["Table"], calculateFontSize(TEXT_SCALES["TableContent"], screenSize), 'normal'), 
                                   text=lst[i][j], borderwidth=border_thickness, relief='solid', anchor='center',
                                   wraplength=wraplength, justify='center', background='#ffffff')
                self.e.grid(row=i, column=j, padx=0, pady=0, sticky='nsew', ipadx=iPadding, ipady=iPadding)

        # Adjust columns to have the same minimum width
        for j in range(total_columns):
            parent.grid_columnconfigure(j, weight=1, minsize=min_cell_width)
        # Adjust lines to have the same height
        for i in range(total_rows):
            parent.grid_rowconfigure(i, weight=1)

class learnScreen(ttk.Frame, Child):
    def __init__(self, parent, screenSize):
        ttk.Frame.__init__(self, parent)
        self.setParent(parent)
        self.screenSize = screenSize

    def render(self):
        mainFrame = ttk.Frame(self.getParent())
        
        # Center widgets inside main frame
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_rowconfigure(1, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)

        
        
        titleFrame = ttk.Frame(mainFrame)
        titleFrame.grid(row=0, column=0, sticky="S", pady=20)
        
        tableFrame = ttk.Frame(mainFrame)
        tableFrame.grid(row=1, column=0, sticky="N")
        
        title = screenTitle(titleFrame)
        title.setFontSize(calculateFontSize(TEXT_SCALES["ScreenTitle"], self.screenSize))
        title.setContent('Character Mapping')
        title.getInstance().pack(fill='both')

        # Add table widget to tableFrame
        table = Table(tableFrame, self.screenSize)

        mainFrame.pack(expand=True, fill='both')
