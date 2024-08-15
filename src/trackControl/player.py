import pygame
import os
from mido import midifiles
import struct
from tkinter import filedialog
from tkinter import *

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
        os.remove('sound.mid')

    def getBusy(midi):
        return pygame.mixer.music.get_busy()
    
    def pauseMusic(midi):
        pygame.mixer.music.pause()
    
    def unpauseMusic(midi):
        pygame.mixer.music.unpause()

    def downloadMusic(midi, fileName):
        root = Tk()
        root.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Choose a filename for download",filetypes = (("midi files","*.mid"),("all files","*.*")))
        fileName = root.filename
        file = open(fileName, 'wb')

        with midifiles.meta.meta_charset(midi.midiFile.charset):
            header = struct.pack('>hhh', midi.midiFile.type,
                                 len(midi.midiFile.tracks),
                                 midi.midiFile.ticks_per_beat)

            midifiles.midifiles.write_chunk(file, b'MThd', header)

            for track in midi.midiFile.tracks:
                midifiles.midifiles.write_track(file, track)

    def getTime(midi):
        return pygame.mixer.music.get_pos()