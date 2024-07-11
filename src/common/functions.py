'''
Created on 2024-07-11

@author: Pedro Lubaszewski Lima

Module with all the common functions of the project.
'''

from common.dictionaries import SCREEN_MEASURE

def calculateFontSize(textScale, screenSize):
    return int(textScale * int(screenSize[SCREEN_MEASURE["Height"]]))