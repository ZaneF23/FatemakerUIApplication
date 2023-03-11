from tkinter import *
import random
import tkinter

#defining the main window
Fatemaker = Tk()
Fatemaker.title("D&D Fatemaker")
headLabel = Label(Fatemaker, text = "On for a random choice, Off to leave empty")
headLabel.pack()

#defines variables for the radio buttons
c = IntVar()
s = IntVar()
l = IntVar()
a = IntVar()

#label for class buttons
classLabel = Label(Fatemaker, text = "Class")
classLabel.pack()

#radio buttons for class
classYes = Radiobutton(Fatemaker, text = "On", variable = c, value = 1)
classYes.pack()
c.set(1)
classNo = Radiobutton(Fatemaker, text = "Off", variable = c, value = 2)
classNo.pack()

#label for species buttons
speciesLabel = Label(Fatemaker, text = "Species")
speciesLabel.pack()

#radio buttons for species
speciesYes = Radiobutton(Fatemaker, text = "On", variable = s, value = 1)
speciesYes.pack()
s.set(1)
speciesNo = Radiobutton(Fatemaker, text = "Off", variable = s, value = 2)
speciesNo.pack()

#label for level buttons
levelLabel = Label(Fatemaker, text = "Level")
levelLabel.pack()

#radio buttons for level
levelYes = Radiobutton(Fatemaker, text = "On", variable = l, value = 1)
levelYes.pack()
l.set(1)
levelNo = Radiobutton(Fatemaker, text = "Off", variable = l, value = 2)
levelNo.pack()

#label for scores buttons
scoresLabel = Label(Fatemaker, text = "Scores")
scoresLabel.pack()

#radio buttons for scores
scoresYes = Radiobutton(Fatemaker, text = "On", variable = a, value = 1)
scoresYes.pack()
a.set(1)
scoresNo = Radiobutton(Fatemaker, text = "Off", variable = a, value = 2)
scoresNo.pack()

#defines the generate function for the generate button
def generate():
    #creates secondary window for information to print to
    charWindow = tkinter.Toplevel()
    charWindow.title("Character Sheet")
    charSheet = Text(charWindow, height = 10, width = 20)
    charSheet.pack()

    #lists to use for random determination of class and species
    classList = ["Artificer", "Barbarian", "Bard", "Blood Hunter", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    speciesList = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]

    #if class is set to on, generates a random class
    if c.get() == 1:
        classNum = random.randint(0,13)
        charClass = classList[classNum]
        charSheet.insert(END, "Class: " + charClass)

    #if species is set to on, generates a random species
    if s.get() == 1:
        speciesNum = random.randint(0,8)
        charSpecies = speciesList[speciesNum]
        charSheet.insert(END, "\nSpecies: " + charSpecies)
    
    #if level is set to on, generates a random level
    if l.get() == 1:
        levelNum = random.randint(1,20)
        charLevel = str(levelNum)
        charSheet.insert(END, "\nLevel: " + charLevel)

    #if scores is set to on, generates random scores following typical rules of 4d6 drop the lowest
    if a.get() == 1:
        strengthNum = random.randint(8,18)
        strength = str(strengthNum)
        dexNum = random.randint(8,18)
        dex = str(dexNum)
        conNum = random.randint(8,18)
        con = str(conNum)
        intelNum = random.randint(8,18)
        intel = str(intelNum)
        wisNum = random.randint(8,18)
        wis = str(wisNum)
        chaNum = random.randint(8,18)
        cha = str(chaNum)
        charSheet.insert(END, "\nScores: ")
        charSheet.insert(END, "\nStrength - " + strength)
        charSheet.insert(END, "\nDexterity - " + dex)
        charSheet.insert(END, "\nConstitution - " + con)
        charSheet.insert(END, "\nIntelligence - " + intel)
        charSheet.insert(END, "\nWisdom - " + wis)
        charSheet.insert(END, "\nCharisma - " + cha)

    #defines reset function for reset button
    def reset():
        charWindow.destroy()
        c.set(1)
        s.set(1)
        l.set(1)
        a.set(1)

    #reset button, which deletes the secondary window and sets all radio buttons back to on
    resetButton = tkinter.Button(charWindow, text = "Reset", width = 10, command = reset)
    resetButton.pack()

#generate button, which opens the secondary window, and randomly generates each selected aspect of the character
genButton = tkinter.Button(Fatemaker, text = "Generate", width = 10, command = generate)
genButton.pack()

#close button, which closes the program
closeButton = tkinter.Button(Fatemaker, text = "Close", width = 10, command = Fatemaker.destroy)
closeButton.pack()

#main loop, to run the program
mainloop()

