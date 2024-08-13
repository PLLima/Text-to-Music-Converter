import mido
from mido import MidiFile, MidiTrack, Message

class midiGen:
    def __init__(self,bpm,opList):
        if bpm == None:
            self.bpm = 120
        else:
            if bpm < 1:
                self.bpm = 1
            elif bpm > 1000:
                self.bpm = 1000
            else:
                self.bpm = bpm
        self.opList = opList


    def gerMidi(param):
        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)
        bpm = param.bpm
        track.append(mido.MetaMessage(type='set_tempo',tempo = mido.bpm2tempo(bpm)))

        for op in range(1, len(param.opList)):
            if param.opList[op][1] == "Note":
                track.append(Message('note_on', note=param.opList[op][0], velocity=param.opList[op][2], time=240 ))
                track.append(Message('note_off', note=param.opList[op][0], velocity=param.opList[op][2], time=240))
            elif param.opList[op][1] == "Instrument":
                track.append(Message('program_change', program = param.opList[op][0], time = 0))
            elif param.opList[op][1] == "Telephone":
                track.append(Message('program_change', program = 124, time = 0))
                track.append(Message('note_on', note=param.opList[op][0], velocity=param.opList[op][2], time=240 ))
                track.append(Message('note_off', note=param.opList[op][0], velocity=param.opList[op][2], time=240))
                track.append(Message('program_change', program = param.opList[op][2], time = 0))
            elif param.opList[op][1] == "BPMPlus":
                bpm += 80
                track.append(mido.MetaMessage(type='set_tempo',tempo = mido.bpm2tempo(bpm)))
            elif param.opList[op][1] == "RandomBPM":
                bpm = param.opList[op][0]
                track.append(mido.MetaMessage(type='set_tempo',tempo = mido.bpm2tempo(bpm)))

        x = bool(1)
        return True, mid
        #mid.save('output.mid')