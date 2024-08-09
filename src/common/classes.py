'''
Created on 2024-07-10

@author: Pedro Lubaszewski Lima

Module with all the common classes of the project.
'''

class Child():
    def setParent(self, parent):
        self.__parent = parent

    def getParent(self):
        return self.__parent

class Closeable():
    def close(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
    

class WindowSizeNotifier():
    def __init__(self, window, eventHandler):
        self.__window = window
        self.__eventHandler = eventHandler
        self.__window.bind('<Configure>', self.__handleEvent)

    def __handleEvent(self, event):
        if event.widget == self.__window:
            self.__eventHandler()