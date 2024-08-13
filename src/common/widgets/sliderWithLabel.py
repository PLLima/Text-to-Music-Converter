import tkinter as tk
from tkinter import ttk
from common.widgets.slider import sliderModel
from common.dictionaries import FONTS, FONT_SIZES

class sliderWithLabel(ttk.Frame):
    def __init__(self, parent, from_=0, to=100, length=200, command=None, initial_value=None, orient='horizontal', font_size=FONT_SIZES["SliderLabel"], **kwargs):
        super().__init__(parent, **kwargs)

        self.from_ = from_
        self.to = to

        # Define the font size and style
        self.font = (FONTS["SliderLabel"], FONT_SIZES["SliderLabel"])

        # Create StringVars for labels
        self.label_left_var = tk.StringVar()
        self.label_right_var = tk.StringVar()

        # Create label to the left
        self.label_left = tk.Label(self, textvariable=self.label_left_var, font=self.font, width=6, anchor='e')
        self.label_left.pack(side=tk.LEFT, padx=(10, 5))

        # Create label to the right
        self.label_right = tk.Label(self, textvariable=self.label_right_var, font=self.font, width=6, anchor='w')
        self.label_right.pack(side=tk.RIGHT, padx=(5, 10))

        # Create slider model
        self.slider = sliderModel(
            self,
            from_=from_,
            to=to,
            length=length,
            command=self._update_labels,
            orient=orient
        )
        self.slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 10))

        # Set the initial value for the slider
        if initial_value is not None:
            self.slider.set(initial_value)
        else:
            initial_value = self.from_

        # Set initial values for labels
        self._update_labels(initial_value)

    def _update_labels(self, value):
        # Formats labels to integers
        value = int(float(value))
        self.label_left_var.set(str(value))
        self.label_right_var.set(str(self.to))

    def set_command(self, command):
        self.slider.set_command(command)

    def set_initial_value(self, value):
        self.slider.set_initial_value(value)
        self._update_labels(value)

    def get_initial_value(self):
        return self.slider.get_initial_value()
