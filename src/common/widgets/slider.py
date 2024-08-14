import tkinter as tk
from tkinter import ttk
from common.classes import Child
from common.dictionaries import SCREEN_COLORS, SLIDER_COLORS, FONTS, FONT_SIZES

class sliderModel(ttk.Scale):
    def __init__(self, parent, from_=0, to=100, length=200, command=None, initial_value=None, orient='horizontal', **kwargs):
        super().__init__(parent, from_=from_, to=to, length=length, orient=orient, **kwargs)

        # Stores slider callback
        self.setSliderCallback(command)

        # Personalized style to remove background and numbers
        style = ttk.Style()
        style.layout('TScale', [
            ('Trough', {
                'children': [('Scale.slider', {'side': 'left', 'sticky': ''})],
                'sticky': 'nswe'
            })
        ])
        self.configure(style="TScale")

        # Selector configuration
        if initial_value is not None:
            self.set(initial_value)

    def setSliderCallback(self, sliderCallback):
        self.__sliderCallback = sliderCallback
        if sliderCallback is not None:
            self.configure(command=sliderCallback)

    def getSliderCallback(self):
        return self.__sliderCallback

    def setValue(self, value):
        self.set(value)

    def getValue(self):
        return self.get()

class sliderWithLabel(tk.Frame):
    def __init__(self, parent, from_=0, to=100, length=200, command=None, initial_value=None, orient='horizontal', font_size=FONT_SIZES["SliderLabel"], **kwargs):
        super().__init__(parent, bg=SCREEN_COLORS["Background"])

        self.from_ = from_
        self.to = to

        # Define the font size and style
        self.font = (FONTS["SliderLabel"], FONT_SIZES["SliderLabel"])

        # Create StringVars for labels
        self.label_left_var = tk.StringVar()
        self.label_right_var = tk.StringVar()

        # Create label to the left
        self.label_left = tk.Label(self, textvariable=self.label_left_var, font=self.font, fg= SLIDER_COLORS["Foreground"],
                                   bg=SCREEN_COLORS["Background"], width=6, anchor='e')
        self.label_left.pack(side=tk.LEFT, padx=(10, 5))

        # Create label to the right
        self.label_right = tk.Label(self, textvariable=self.label_right_var, font=self.font, fg= SLIDER_COLORS["Foreground"],
                                    bg=SCREEN_COLORS["Background"], width=6, anchor='w')
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
            self.slider.setValue(initial_value)
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
        self.slider.setSliderCallback(command)

    def set_initial_value(self, value):
        self.slider.setValue(value)
        self._update_labels(value)

    def get_initial_value(self):
        return self.slider.getValue()
    
class paramSlider(tk.Frame, sliderModel, Child):
    def __init__(self, parent, from_=0, to=100, length=200, command=None, initial_value=None, orient='horizontal'):
        self.setParent(parent)
        tk.Frame.__init__(self, self.getParent(), bg=SCREEN_COLORS["Background"])
        self.__setInstance()

    def __setInstance(self):
        self.__instance = sliderModel.__init(self, from_=0, to=100, length=200,
                                             command=None, initial_value=None, orient='horizontal')

    def getInstance(self):
        return self.__instance