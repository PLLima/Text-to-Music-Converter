from common.classes import Child
from screens.start import startScreen
from screens.learnMore import learnScreen
from screens.initialParameters import paramsScreen
#from screens.musicPlayer import playerScreen

class appController(Child):
    def __init__(self, app):
        self.setParent(app.getParent())
        self.__setScreenSize(app.getAppScreenSize())
        self.__startScreen = None
        self.__learnScreen = None
        self.__paramsScreen = None
        self.__playerScreen = None

    def __setScreenSize(self, screenSize):
        self.__screenSize = screenSize

    def getScreenSize(self):
        return self.__screenSize
    
    def __setStartScreen(self, startScreen):
        self.__startScreen = startScreen

    def __getStartScreen(self):
        return self.__startScreen

    def renderStartScreen(self):
        self.__setStartScreen(startScreen(self))
        self.__getStartScreen().render()

    def __setLearnScreen(self, learnScreen):
        self.__learnScreen = learnScreen

    def __getLearnScreen(self):
        return self.__learnScreen

    def renderLearnScreen(self):
        self.__setLearnScreen(learnScreen(self))
        self.__getLearnScreen().render()

    def __setParamsScreen(self, paramsScreen):
        self.__paramsScreen = paramsScreen

    def __getParamsScreen(self):
        return self.__paramsScreen

    def renderParamsScreen(self):
         self.__setParamsScreen(paramsScreen(self))
         self.__getParamsScreen().render()

    def __setPlayerScreen(self, playerScreen):
        self.__playerScreen = playerScreen

    def __getPlayerScreen(self):
        return self.__playerScreen

    # def renderPlayerScreen(self):
    #     self.__selfPlayerScreen(playerScreen(self))
    #     self.__getPlayerScreen().render()