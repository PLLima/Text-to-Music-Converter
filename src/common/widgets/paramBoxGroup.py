import tkinter as tk
from common.widgets.paramBox import paramBox
from common.dictionaries import SCREEN_COLORS, FONTS, FONT_SIZES

class paramBoxGroup(tk.Frame):
    def __init__(self, parent, volume="75%", bpm="250", octave="C2", *args, **kwargs):
        super().__init__(parent, bg=SCREEN_COLORS["Background"], *args, **kwargs)
        self.createBoxGroup(volume, bpm, octave)

    def createBoxGroup(self, volume, bpm, octave):
        # Create and place paramBox widgets
        self.box1 = paramBox(
            self, 
            line1="Volume", 
            line2=volume, 
            width=100, 
            height=100, 
            font_family=FONTS["Parambox"], 
            font_size=FONT_SIZES["Boxes"], 
            font_color="#636363",
            bg='#D9D9D9',
            border_color="#636363", 
            border_width=0.5 
        )
        
        self.box2 = paramBox(
            self, 
            line1="BPM", 
            line2=bpm, 
            width=100, 
            height=100, 
            font_family=FONTS["Parambox"], 
            font_size=FONT_SIZES["Boxes"], 
            font_color="#636363",
            bg='#D9D9D9',
            border_color="#636363", 
            border_width=0.5 
        )
        
        self.box3 = paramBox(
            self, 
            line1="Octave", 
            line2=octave, 
            width=100, 
            height=100, 
            font_family=FONTS["Parambox"], 
            font_size=FONT_SIZES["Boxes"], 
            font_color="#636363",
            bg='#D9D9D9',
            border_color="#636363", 
            border_width=0.5 
        )

        # Grid configuration with left and right margins
        margin_left = 95  # Define the margin here
        margin_right = 40  # Define the right margin here
        space = 20         # Space between Boxes
        self.box1.grid(row=0, column=0, columnspan=2, sticky="NSEW", pady=(0, space), padx=(margin_left, margin_right))
        self.box2.grid(row=1, column=0, columnspan=2, sticky="NSEW", pady=space/2, padx=(margin_left, margin_right))
        self.box3.grid(row=2, column=0, columnspan=2, sticky="NSEW", pady=(space, 0), padx=(margin_left, margin_right))

        # Configure rows and columns to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Set minimum size for columns if needed
        self.grid_columnconfigure(0, minsize=100)
        self.grid_columnconfigure(1, minsize=100)
