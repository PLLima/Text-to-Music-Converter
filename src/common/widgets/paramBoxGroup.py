import tkinter as tk
from common.widgets.paramBox import paramBox
from common.dictionaries import FONTS

class paramBoxGroup(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.createBoxGroup()

    def createBoxGroup(self):
        # Create and place paramBox widgets
        self.box1 = paramBox(
            self, 
            line1="Volume", 
            line2="75%", 
            width=100, 
            height=100, 
            font_family=FONTS["Parambox"], 
            font_size=14, 
            font_weight="bold", 
            font_color="#636363",
            bg='#D9D9D9',
            border_color="#636363", 
            border_width=0.5 
        )
        
        self.box2 = paramBox(
            self, 
            line1="BPM", 
            line2="250", 
            width=100, 
            height=100, 
            font_family=FONTS["Parambox"], 
            font_size=14, 
            font_weight="bold", 
            font_color="#636363",
            bg='#D9D9D9',
            border_color="#636363", 
            border_width=0.5 
        )
        
        self.box3 = paramBox(
            self, 
            line1="Octave", 
            line2="C2", 
            width=100, 
            height=100, 
            font_family=FONTS["Parambox"], 
            font_size=14, 
            font_weight="bold", 
            font_color="#636363",
            bg='#D9D9D9',
            border_color="#636363", 
            border_width=0.5 
        )

        # Grid configuration with left margin
        margin_left = 20  # Define the margin here
        self.box1.grid(row=0, column=0, columnspan=2, sticky="NSEW", pady=10, padx=(margin_left, 0))
        self.box2.grid(row=1, column=0, columnspan=2, sticky="NSEW", pady=10, padx=(margin_left, 0))
        self.box3.grid(row=2, column=0, columnspan=2, sticky="NSEW", pady=10, padx=(margin_left, 0))

        # Configure rows and columns to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
