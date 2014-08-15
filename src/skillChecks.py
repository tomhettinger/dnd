#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import random

class skillChecks(Tkinter.Tk):

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def roll(self, dice):
        result = 0
        for i in range(dice[0]):
            result += random.randint(1,dice[1])
        return result

    def makeLabel(self, text="NEW", x=0, y=0, length=1, width=4, bg='green'):
        labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=labelVariable, anchor="w", fg="black", bg=bg, width=width)
        label.grid(column=x, row=y, columnspan=length, sticky='EW')
        labelVariable.set(text)
        return labelVariable

    def makeAtk(self, weapon='Weapon', x=0, y=0, cmd=None):
        button = Tkinter.Button(self, text=weapon, command=cmd)
        button.grid(column=x, row=y)

    def makeField(self, text, x, y):
        entryVariable = Tkinter.IntVar()
        entry = Tkinter.Entry(self, textvariable=entryVariable, width=3)
        entry.grid(column=x,row=y,sticky='EW')
        #entry.bind("<Return>", self.OnPressEnter)
        entryVariable.set(text)
        return entryVariable

    def makeCheck(self, txt, x, y):
        var = Tkinter.IntVar()
        c = Tkinter.Checkbutton(self, text=txt, variable=var)
        c.grid(column=x, row=y)
        var.set(0)
        return var

    def initialize(self):
        self.grid()

        
        self.skillName = ["Appraise", "Balance", "Bluff", "Climb", "Concentration", "Craft (Bowmaking)", "Decipher Script", 
                    "Diplomacy", "Disable Device", "Disguise", "Escape Artist", "Forgery", "Gather Info", "Handle Animal", 
                    "Heal", "Hide", "Intimidate", "Jump", "Knowl (Dungeoneering)", "Knowl (Geography)", "Know (Nature)", 
                    "Listen", "Move Silently", "Open Lock", "Perform ()", "Prof. (Hunter)", "Ride", "Search", "Sense Motive", 
                    "Sleight of Hand", "Spellcraft", "Spot", "Survival", "Swim", "Tumble", "Use Magic Device", "Use Rope", "Wild Empathy"]

        self.skillStats = [0, 2, 0, 4, 1, 6, ' ',
                           0, ' ', 1, 2, 0, 0, 3, 
                           3, 2, 1, 0, 1, 1, 5, 
                           8, 2, 5, ' ', 1, 1, 4, 1,
                           3, 1, 8, 1, -2, 3, ' ', 8, 6]  # blank space indicates untrained

        self.isClassSkill = [0, 0, 0, 1, 1, 1, 0, 
                        0, 0, 0, 0, 0, 0, 1, 
                        1, 1, 0, 1, 1, 1, 1, 
                        1, 1, 0, 0, 1, 1, 1, 0,
                        0, 0, 1, 1, 1, 0, 0, 1, 0]
        # Skill Labels
        for i in range(len(self.skillName)):
            self.makeLabel(self.skillName[i], 0, i+1, 1, 20)

        # Skill Bonus
        for i in range(len(self.skillName)):
            self.makeLabel(self.skillStats[i], 1, i+1, 1, 4)

        # Roll Result
        self.makeLabel('Roll', 2, 0)
        self.fields = []
        for i in range(len(self.skillName)):
            self.fields.append( self.makeField(self.skillStats[i], 2, i+1) )

        # Class Skills
        for i in range(len(self.skillName)):
            if self.isClassSkill[i]:
                self.makeLabel("Class Skill", 3, i+1, 1, 8, 'Yellow')

        # Armor Check
        for i in range(len(self.skillName)):
            if i in [1, 3, 10, 15, 17, 22, 29, 33, 34] :
                self.makeLabel("Armor", 4, i+1, 1, 8, 'Blue')

        # Uncivilized
        for i in range(len(self.skillName)):
            if i in [2, 7, 12, 13, 38] :
                self.makeLabel("Uncivilized", 4, i+1, 1, 8, 'White')

        # Avoided
        for i in range(len(self.skillName)):
            if i in [26] :
                self.makeLabel("Avoided", 4, i+1, 1, 8, 'Orange')

        # Natural Roll
        self.makeLabel('Nat', 5, 0)
        self.natural = []
        for i in range(len(self.skillName)):
            self.natural.append( self.makeField(' ', 5, i+1) )

        # Roll Button
        self.makeAtk("Roll Many D20", 6, 0, self.rollAttack1)
        self.isBow   = self.makeCheck("is Bow", 6, 1)
        self.isAboveGround = self.makeCheck("above ground", 6, 32)
        self.isFavored = self.makeCheck("Favored or Pouch", 0, 0)

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())

    def rollAttack1(self):     # Roll a D20 for skill check
        for i in range(len(self.skillName)):
            if self.skillStats[i] != ' ':
                roll = self.roll([1,20])
                self.natural[i].set(roll)
                result = self.skillStats[i] + roll
                if i in [2, 21, 28, 31, 32]:         # if Favored matters
                    result += 2*self.isFavored.get()
                if i == 31:                           # if doing a spot
                    result += 2*self.isAboveGround.get()
                if i == 0:                            # if appraising
                    result += 2*self.isBow.get()
                self.fields[i].set(result)

if __name__ == "__main__":
    app = skillChecks(None)
    app.title('Skill Checks')
    app.mainloop()

