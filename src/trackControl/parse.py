import random

class parseText:
    def __init__(self,octave,volume,characters):
        if octave == None:
            self.octave = 0
        else:
            if octave > 4:
                octave = 4
            elif octave < -4:
                octave = -4
            else:
                self.octave = octave
        if volume == None or volume < 0:
            self.volume = 64
        else:
            if volume > 126:
                self.volume = 126
            else:
                self.volume = volume
        self.characters = characters

    def parserText(text):
        opList = []
        octave = text.octave
        volume = text.volume
        lastNote = 0
        lastCommand = 0
        instrument = 0
        skipCounter = 0

        NOTES = {
            "Do" : 60, #C
            "Re" : 62, #D
            "Mi" : 64, #E
            "Fa" : 65, #F
            "Sol": 67, #G
            "La" : 69, #A
            "Si" : 71, #B
            "Not" : 0, #Silence
        }

        for i in range(0, len(text.characters)):
            if skipCounter > 0:
                skipCounter -= 1
                continue
            if text.characters[i] == 'B':
                if text.characters[i+1] != None and text.characters[i+1] == 'P':
                    skipCounter = 3
                    opList.append((0,"BPMPlus"))
                lastCommand = "NotNote"
            elif text.characters[i].lower() == 'c':
                opList.append((NOTES["Do"] + (octave * 12),"Note",volume))
                lastNote = "Do"
                lastCommand = "Note"
            elif text.characters[i].lower() == 'd':
                opList.append((NOTES["Re"] + (octave * 12),"Note",volume))
                lastNote = "Re"
                lastCommand = "Note"
            elif text.characters[i].lower() == 'e':
                opList.append((NOTES["Mi"] + (octave * 12),"Note",volume))
                lastNote = "Mi"
                lastCommand = "Note"
            elif text.characters[i].lower() == 'f':
                opList.append((NOTES["Fa"] + (octave * 12),"Note",volume))
                lastNote = "Fa"
                lastCommand = "Note"
            elif text.characters[i].lower() == 'g':
                opList.append((NOTES["Sol"] + (octave * 12),"Note",volume))
                lastNote = "Sol"
                lastCommand = "Note"
            elif text.characters[i].lower() == 'a':
                opList.append((NOTES["La"] + (octave * 12),"Note",volume))
                lastNote = "La"
                lastCommand = "Note"
            elif text.characters[i].lower() == 'b':
                opList.append((NOTES["Si"] + (octave * 12),"Note",volume))
                lastNote = "Si"
                lastCommand = "Note"
            elif text.characters[i] == ' ':
                opList.append((NOTES["Not"],"Note",0))
                lastCommand = "NotNote"
            elif text.characters[i] == '+':
                lastCommand = "NotNote"
                volume = volume * 2
                if volume > 127:
                    volume = 127
            elif text.characters[i] == '-':
                lastCommand = "NotNote"
                volume = text.volume
            elif text.characters[i].lower() == 'o' or text.characters[i].lower() == 'i' or text.characters[i].lower() == 'u':
                if lastCommand == "Note":
                    opList.append((NOTES[lastNote] + (octave * 12),"Note",volume))
                else:
                    opList.append((NOTES[lastNote] + (octave * 12),"Telephone",instrument))
                lastCommand = "NotNote"
            elif text.characters[i] == 'R':
                if text.characters[i+1] != None and text.characters[i+1] == '+':
                    skipCounter = 1
                    if octave < 4:
                        octave += 1
                    else:
                        octave = 4 
                if text.characters[i+1] != None and text.characters[i+1] == '-':
                    skipCounter = 1
                    if octave > -4:
                        octave -= 1
                    else:
                        octave = -4
                lastCommand = "NotNote"
            elif text.characters[i] == '?':
                note = random.randrange(1,7,1)
                if note == 1:
                    opList.append((NOTES["Do"] + (octave * 12),"Note",volume))
                elif note == 2:
                    opList.append((NOTES["Re"] + (octave * 12),"Note",volume))
                elif note == 3:
                    opList.append((NOTES["Mi"] + (octave * 12),"Note",volume))
                elif note == 4:
                    opList.append((NOTES["Fa"] + (octave * 12),"Note",volume))
                elif note == 5:
                    opList.append((NOTES["Sol"] + (octave * 12),"Note",volume))
                elif note == 6:
                    opList.append((NOTES["La"] + (octave * 12),"Note",volume))
                elif note == 7:
                    opList.append((NOTES["Si"] + (octave * 12),"Note",volume))
                lastCommand = "NotNote"
            elif text.characters[i] == '\n':
                instrument = (random.randrange(0,127,1))
                opList.append((instrument,"Instrument"))
                lastCommand = "NotNote"
            elif text.characters[i] == ';':
                opList.append(((random.randrange(1,1000,1)),"RandomBPM"))
                lastCommand = "NotNote"
        return opList
