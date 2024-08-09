from common.dictionaries import SCREEN_MEASURE

def calculateFontSize(textScale, screenSize):
    return int(textScale * int(screenSize[SCREEN_MEASURE["Height"]]))