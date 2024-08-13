import tkinter as tk
from tkinter import ttk
from common.widgets.slider import sliderModel

class sliderWithLabel(ttk.Frame):
    def __init__(self, parent, from_=0, to=100, length=200, command=None, initial_value=None, orient='horizontal', **kwargs):
        super().__init__(parent, **kwargs)

        self.from_ = from_
        self.to = to

        # Cria a Label à esquerda
        self.label_left = tk.Label(self, text=str(int(initial_value if initial_value is not None else from_)))
        self.label_left.pack(side=tk.LEFT)

        # Cria a Label à direita
        self.label_right = tk.Label(self, text=str(int(to)))
        self.label_right.pack(side=tk.RIGHT)

        # Cria o sliderModel
        self.slider = sliderModel(
            self,
            from_=from_,
            to=to,
            length=length,
            command=self._update_labels,
            orient=orient
        )
        self.slider.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Atualiza o valor da Label quando o slider é movido
        if initial_value is not None:
            self.slider.set(initial_value)
            self._update_labels(initial_value)

    def _update_labels(self, value):
        # Formata o valor para ser um inteiro
        value = int(float(value))
        self.label_left.config(text=str(value))
        self.label_right.config(text=str(self.to))

    def set_command(self, command):
        self.slider.set_command(command)

    def set_initial_value(self, value):
        self.slider.set_initial_value(value)
        self._update_labels(value)

    def get_initial_value(self):
        return self.slider.get_initial_value()
