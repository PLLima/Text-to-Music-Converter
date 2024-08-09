class Child():
    def setParent(self, parent):
        self.__parent = parent

    def getParent(self):
        return self.__parent

class WindowSizeNotifier():
    def __init__(self, window, eventHandler):
        self.__window = window
        self.__eventHandler = eventHandler
        self.__window.bind('<Configure>', self.__handleEvent)

    def __handleEvent(self, event):
        if event.widget == self.__window:
            self.__eventHandler()