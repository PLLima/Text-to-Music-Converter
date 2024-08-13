import tkinter as tk
from tkinter import ttk

class sliderModel(ttk.Scale):
    def __init__(self, parent, from_=0, to=100, length=200, command=None, initial_value=None, orient='horizontal', **kwargs):
        super().__init__(parent, from_=from_, to=to, length=length, command=self._internal_command, orient=orient, **kwargs)

        self.user_command = command  # Armazena o comando passado pelo usuário

        # Estilo personalizado para remover números e fundo
        style = ttk.Style()
        style.layout('TScale', [
            ('Trough', {
                'children': [('Scale.slider', {'side': 'left', 'sticky': ''})],
                'sticky': 'nswe'
            })
        ])
        self.configure(style="TScale")

        # Configuração do seletor
        if initial_value is not None:
            self.set(initial_value)

    def _internal_command(self, value):
        # Chama o comando do usuário, se houver, com apenas um argumento (valor)
        if self.user_command:
            self.user_command(value)

    def set_command(self, command):
        self.user_command = command
        self.configure(command=self._internal_command)

    def set_initial_value(self, value):
        self.set(value)

    def get_initial_value(self):
        return self.get()
