import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from common.classes import Child
from common.dictionaries import SCREEN_COLORS, SLIDER_COLORS, FONTS, FONT_SIZES

class sliderModel(ttk.Scale):
    def __init__(self, parent, minValue=0, maxValue=100, length=200, command=None, initialValue=None, orient='horizontal', **kwargs):
        # Altere os parâmetros minValue e maxValue para from_ e to
        super().__init__(parent, from_=minValue, to=maxValue, length=length, orient=orient, **kwargs)

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
        if initialValue is not None:
            self.set(initialValue)

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
    def __init__(self, parent, minValue=0, maxValue=100, length=100, command=None, initialValue=0, orient='horizontal', font_size=FONT_SIZES["SliderLabel"], **kwargs):
        super().__init__(parent, bg=SCREEN_COLORS["Background"])

        self.minValue = minValue
        self.maxValue = maxValue

        # Define the font size and style
        self.font = (FONTS["SliderLabel"], FONT_SIZES["SliderLabel"])

        # Create StringVars for labels
        self.labelLeftVar = tk.StringVar()
        self.labelRightVar = tk.StringVar()

        # Create label to the left
        self.labelLeft = tk.Label(self, textvariable=self.labelLeftVar, font=self.font, fg= SLIDER_COLORS["Foreground"],
                                   bg=SCREEN_COLORS["Background"], width=6, anchor='e')
        self.labelLeft.pack(side=tk.LEFT, padx=(10, 5))

        # Create label to the right
        self.labelRight = tk.Label(self, textvariable=self.labelRightVar, font=self.font, fg= SLIDER_COLORS["Foreground"],
                                    bg=SCREEN_COLORS["Background"], width=6, anchor='w')
        self.labelRight.pack(side=tk.RIGHT, padx=(5, 10))

        # Create slider model
        self.slider = sliderModel(
            self,
            minValue=minValue,
            maxValue=maxValue,
            length=length,
            command=self.updateLabels,
            orient=orient
        )
        self.slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 10))

        # Set the initial value for the slider
        if initialValue is not None:
            self.slider.setValue(initialValue)
        else:
            initialValue = self.minValue

        # Set initial values for labels
        self.updateLabels(initialValue)

    def updateLabels(self, value):
        # Formats labels maxValue integers
        value = int(float(value))
        self.labelLeftVar.set(self.formatTime(value))
        self.labelRightVar.set(self.formatTime(self.maxValue))

    def formatTime(self, time):
        min = 0
        while time >=60:
            time -= 60
            min+=1
        if time < 10:
            time = "0"+str(time)
        return str(min)+":"+str(time)

    def set_command(self, command):
        self.slider.setSliderCallback(command)

    def setValue(self, value):
        self.slider.setValue(value)
        self.updateLabels(value)

    def getValue(self):
        return self.slider.getValue()
    
    
    def enable(self):
        self.slider.config(state=tk.NORMAL)
    
    def disable(self):
        self.slider.config(state=tk.DISABLED)

class paramSlider(tk.Frame, Child):
    def __init__(self, parent, minValue, maxValue, initialValue, fontSize, isPercentage):
        self.setParent(parent)
        tk.Frame.__init__(self, self.getParent(), bg=SCREEN_COLORS["Background"])
        if isPercentage == False:
            self.__disablePercentage()
        else:
            self.__enablePercentage()
        self.__setMaxValue(maxValue)
        self.setTitleText('', 1)
        self.__createLabel(initialValue, fontSize)
        self.setTextPadding(0, 0)
        self.__setSlider(minValue, maxValue, initialValue)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

    def setTextPadding(self, padxLeft, padxRight):
        self.__padxLeft = padxLeft
        self.__padxRight = padxRight
        self.__getTitle().grid(row=0, column=0, sticky="E", padx=(0, self.getTextPaddingLeft()))
        self.__getLabel().grid(row=0, column=2, sticky="W", padx=(self.getTextPaddingRight(), 0))

    def getTextPaddingLeft(self):
        return self.__padxLeft

    def getTextPaddingRight(self):
        return self.__padxRight

    def __setMaxValue(self, maxValue):
        self.__maxValue = maxValue

    def __getMaxValue(self):
        return self.__maxValue

    def __setSlider(self, minValue, maxValue, initialValue):
        self.__slider = sliderModel(self, minValue=minValue, maxValue=maxValue, command=self.__onSlideChange,
                                           initialValue=initialValue, orient='horizontal')
        self.__getSlider().grid(row=0, column=1, sticky="EW")

    def __getSlider(self):
        return self.__slider

    def __setTitle(self, title, fontSize):
        titleFont = tkFont.Font(family=FONTS["SliderLabel"], size=fontSize, weight='bold')
        self.__title = tk.Label(self, text=title, font=titleFont, bg=SCREEN_COLORS["Background"], fg=SLIDER_COLORS["Foreground"])

    def __getTitle(self):
        return self.__title

    def setTitleText(self, text, fontSize):
        self.__titleText = text
        self.__setTitle(text, fontSize)

    def getTitleText(self):
        return self.__titleText

    def getSliderValue(self):
        return int(self.__getSlider().getValue())

    def __enablePercentage(self):
        self.__isPercentage = True
    
    def __disablePercentage(self):
        self.__isPercentage = False

    def __getPercentage(self):
        return self.__isPercentage

    def __createLabel(self, initialValue, fontSize):
        labelFont = tkFont.Font(family=FONTS["SliderLabel"], size=fontSize)
        self.__labelVar = tk.StringVar()
        self.__setLabelVar(initialValue)
        if self.__getPercentage() == False:
            labelLength = len(str(self.__getMaxValue()))
        else:
            labelLength = len(str(self.__getMaxValue())) + 1
        self.__label = tk.Label(self, textvariable= self.__getLabelVar(), font=labelFont, width=labelLength,
                                bg=SCREEN_COLORS["Background"], fg=SLIDER_COLORS["Foreground"])

    def __getLabel(self):
        return self.__label

    def __setLabelVar(self, value):
        stringValue = str(int(float(value)))
        if self.__getPercentage() == False:
            self.__getLabelVar().set(stringValue)
        else:
            self.__getLabelVar().set(stringValue + '%')

    def __getLabelVar(self):
        return self.__labelVar

    def __onSlideChange(self, value, *args):
        self.__setLabelVar(value)