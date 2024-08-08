'''
Created on 2024-07-09

@author: Pedro Lubaszewski Lima

Module with all the common dictionaries of the project.
'''

SCREEN_MEASURE = {
    "Width": 0,
    "Height": 1,
    }

TEXT_SCALES = {
    "MainHeader": 0.0725,
    "MainSubtitle": 0.029041667,
    "TextButton": 0.030041667,
    "ScreenTitle": 0.0425,
    "TableContent": 0.015,
}

TEXT_SCALES["TableHeader"] = TEXT_SCALES["TableContent"] + 0.005

FONTS = {
    "MainHeader": 'Courier New',
    "MainSubtitle": 'Courier New',
    "TextButton": 'Courier New',
    "Table": 'Courier New',
}

BUTTON_COLORS = {
    "Black": '#000000',
    "Gray": '#636363',
    "Red": '#f66a6a',

    "Foreground": '#ffffff',
    "BlackActive": '#2F2F2F',
    "RedActive": '#FB8585',
}