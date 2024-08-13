import tkinter as tk
import tkinter.font as tkFont

class paramBox(tk.Frame):
    def __init__(self, parent, line1="", line2="", width=200, height=200, font_family="Arial", font_size=12, font_color="#000000", bg='#d9d9d9', border_color="#636363", border_width=2):
        super().__init__(parent, bg=bg, width=width, height=height, bd=0, highlightthickness=0)
        self.line1 = line1
        self.line2 = line2
        self.font_family = font_family
        self.font_size = font_size
        self.font_color = font_color
        self.bg = bg
        self.border_color = border_color
        self.border_width = border_width
        self.setInstance()

    def setInstance(self):
        # Configura a borda do Frame
        self.configure(borderwidth=self.border_width, relief='solid', highlightbackground=self.border_color)

        # Cria um Frame interno para centralizar os Labels
        self.inner_frame = tk.Frame(self, bg=self.bg)
        self.inner_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Configura as fontes para as duas linhas
        self.font_line1 = tkFont.Font(family=self.font_family, size=self.font_size, weight="bold")
        self.font_line2 = tkFont.Font(family=self.font_family, size=self.font_size, weight="normal")

        # Cria os labels para cada linha de texto
        self.label_line1 = tk.Label(self.inner_frame, text=self.line1, font=self.font_line1, bg=self.bg, fg=self.font_color)
        self.label_line2 = tk.Label(self.inner_frame, text=self.line2, font=self.font_line2, bg=self.bg, fg=self.font_color)

        # Posiciona os labels dentro do Frame interno
        self.label_line1.pack()
        self.label_line2.pack()

    def setContent(self, line1, line2):
        self.line1 = line1
        self.line2 = line2
        self.label_line1.config(text=self.line1)
        self.label_line2.config(text=self.line2)

    def setFont(self, font_family=None, font_size=None, font_color=None):
        if font_family:
            self.font_family = font_family
        if font_size:
            self.font_size = font_size
        if font_color:
            self.font_color = font_color

        self.font_line1.config(family=self.font_family, size=self.font_size, weight="bold")
        self.font_line2.config(family=self.font_family, size=self.font_size, weight="normal")
        self.label_line1.config(font=self.font_line1, fg=self.font_color)
        self.label_line2.config(font=self.font_line2, fg=self.font_color)

    def setDimensions(self, width, height):
        self.config(width=width, height=height)
        self.inner_frame.config(width=width, height=height)

    def setBorder(self, border_color=None, border_width=None):
        if border_color:
            self.border_color = border_color
        if border_width is not None:
            self.border_width = border_width
        self.configure(borderwidth=self.border_width, relief='solid', highlightbackground=self.border_color)

    def getContent(self):
        return self.line1, self.line2

    def getFont(self):
        return {
            "family": self.font_family,
            "size": self.font_size,
            "color": self.font_color
        }

    def getDimensions(self):
        return self.winfo_width(), self.winfo_height()

    def getBorder(self):
        return {
            "color": self.border_color,
            "width": self.border_width
        }
