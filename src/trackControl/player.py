import pygame
import os
class setPlayer:
    def __init__(self,midiFile):
        self.midiFile = midiFile

    def getMusicLength(midi):
        return midi.midiFile.length
    
    def loadMusic(midi):
        midi.midiFile.save('sound.mid')
        pygame.init()
        pygame.mixer.music.load("sound.mid")
    
    def playMusic(midi):
        pygame.mixer.music.play()

    def unloadMusic(midi):
        pygame.mixer.music.unload()
        os.remove('output.mid')

    def getBusy(midi):
        return pygame.mixer.music.get_busy()
    
    def pauseMusic(midi):
        pygame.mixer.music.pause()

    def downloadMusic(midi, fileName):
        midi.midiFile.save(fileName + '.mid')