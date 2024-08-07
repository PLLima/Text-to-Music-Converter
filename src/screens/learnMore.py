from common.classes import Child
from common.functions import calculateFontSize
from common.dictionaries import TEXT_SCALES
from common.dictionaries import FONTS
from common.widgets.mainHeader import mainHeader
from common.widgets.mainSubtitle import mainSubtitle
from tkinter import ttk
from tkinter import Label

class Table():
    def __init__(self, root, screenSize):
        # Dados da tabela
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
        

        # Número total de linhas e colunas
        total_rows = len(lst)
        total_columns = len(lst[0])

        # Espessura da borda e largura mínima da célula
        border_thickness = 0.5  # Ajuste a espessura da borda aqui
        min_cell_width = 200  # Largura mínima da célula em pixels
        iPadding = 20 # Padding X e Y interno das labels

        # Código para criar a tabela usando Labels com bordas
        for i in range(total_rows):
            for j in range(total_columns):
                wraplength = min_cell_width  # Defina o valor apropriado para a largura desejada da célula
                if i == 0:
                    self.e = Label(root, fg='#636363', font=(FONTS["Table"], calculateFontSize(TEXT_SCALES["TableContent"], screenSize), 'bold'), 
                                   text=lst[i][j], borderwidth=border_thickness, relief='solid', anchor='center',
                                   wraplength=wraplength, justify='center', background='#DCDCDC')
                else:
                    self.e = Label(root, fg='#636363', font=(FONTS["Table"], calculateFontSize(TEXT_SCALES["TableContent"], screenSize), 'normal'), 
                                   text=lst[i][j], borderwidth=border_thickness, relief='solid', anchor='center',
                                   wraplength=wraplength, justify='center', background='#ffffff')
                self.e.grid(row=i, column=j, padx=0, pady=0, sticky='nsew', ipadx=iPadding, ipady=iPadding)

        # Ajuste das colunas para ter a mesma largura mínima
        for j in range(total_columns):
            root.grid_columnconfigure(j, weight=1, minsize=min_cell_width)
        # Ajuste das linhas para ter a mesma altura
        for i in range(total_rows):
            root.grid_rowconfigure(i, weight=1)

class learnScreen(ttk.Frame, Child):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.setParent(parent)

    def render(self):
        mainFrame = ttk.Frame(self.getParent().getParent())
        
        # Center widgets inside main frame
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_rowconfigure(1, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)

        screenSize = self.getParent().getAppScreenSize()
        
        titleFrame = ttk.Frame(mainFrame)
        titleFrame.grid(row=0, column=0, sticky="N")
        
        tableFrame = ttk.Frame(mainFrame)
        tableFrame.grid(row=1, column=0, sticky="N")
        
        title = mainHeader(titleFrame)
        title.setFontSize(calculateFontSize(TEXT_SCALES["ScreenTitle"], screenSize))
        title.setContent('Character Mapping')
        title.render()

        table = Table(tableFrame, screenSize)  # Adicionando a tabela no tableFrame

        mainFrame.pack(expand=True, fill='both')
