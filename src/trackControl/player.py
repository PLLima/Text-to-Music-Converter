from mido import MidiFile
import pygame
class setPlayer:
    def __init__(self,midiFile):
        self.midiFile = midiFile

    def getMusicLength(midi):
        return midi.midiFile.length
    
    def playMusic(midi):
        midi.midiFile.save('output.mid')

        pygame.init()
        pygame.mixer.music.load("output.mid")
        pygame.mixer.music.play()
        
    def getBusy(midi):
        return pygame.mixer.music.get_busy()