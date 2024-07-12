'''
Created on 2024-07-10

@author: Pedro Lubaszewski Lima

Module with all the common classes of the project.
'''

class Child():
    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent
    
class WindowSizeNotifier():
    def __init__(self, window, eventHandler):
        self.window = window
        self.eventHandler = eventHandler
        self.window.bind('<Configure>', self.__handleEvent)

    def __handleEvent(self, event):
        if event.widget == self.window:
            self.eventHandler()