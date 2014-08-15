#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import random

class roll(Tkinter.Tk):

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def roll(self, dice):
        result = 0
        for i in range(dice[0]):
            result += random.randint(1,dice[1])
        return result

    def makeLabel(self, stat="NEW", x=0, y=0, length=1, width=4, bg='blue'):
        labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=labelVariable, anchor="w", fg="white", bg=bg, width=width)
        label.grid(column=x, row=y, columnspan=length, sticky='EW')
        labelVariable.set(stat)
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

        # Weapon Attacks
        self.makeLabel("Weapon Attacks",           2, 0, 2)
        self.makeAtk("MW Composite Longbow (+2)", 2, 1, self.rollAttack1)
        self.isPointBlank = self.makeCheck("< 30ft", 2, 2)
        self.isRapidShot  = self.makeCheck("Rapid Shots", 3, 2)
        self.makeAtk("MW Longsword",              2, 3, self.rollAttack2)
        self.makeAtk('Shortsword',                2, 5, self.rollAttack3)
        self.raptorArrow = True
        self.isFavored  = self.makeCheck("is Favored", 3, 9)
        self.isFlanking = self.makeCheck("is Flanking", 3, 8)
        self.isCharging = self.makeCheck("is Charging", 4, 8)
        self.isPouch    = self.makeCheck("Spirit Pouch", 4, 9)

        # Roll results
        self.makeLabel("Attack Roll",          3, 0, 1,10)
        self.atk1result = self.makeField(0, 3, 1)
        self.atk2result = self.makeField(0, 3, 3)
        self.atk3result = self.makeField(0, 3, 5)

        # Damage Done
        self.makeLabel("Dmg on Hit",        4, 0, 1,10)
        self.dmg1result = self.makeField(0, 4, 1)
        self.dmg2result = self.makeField(0, 4, 3)
        self.dmg3result = self.makeField(0, 4, 5)

        # Comments
        self.comment1 = self.makeLabel("Ready to Attack", 5, 1, 1, 25, 'red')
        self.comment2 = self.makeLabel("Ready to Attack", 5, 3, 1, 25, 'red')
        self.comment3 = self.makeLabel("Ready to Attack", 5, 5, 1, 25, 'red')

        # Stat Labels
        self.makeLabel("HP ", 0, 0, 1, 4, 'red')        
        self.makeLabel("STR", 0, 1, 1)
        self.makeLabel("DEX", 0, 2, 1)
        self.makeLabel("CON", 0, 3, 1)
        self.makeLabel("INT", 0, 4, 1)
        self.makeLabel("WIS", 0, 5, 1)
        self.makeLabel("CHA", 0, 6, 1)
        self.makeLabel("   ", 0, 7, 1)
        self.makeLabel("Atk", 0, 8, 1)
        self.makeLabel("   ", 0, 9, 1)
        self.makeLabel("AC", 0,10, 1)

        # Stats
        self.HP  = self.makeField(32,1, 0)
        self.STR = self.makeField(2, 1, 1)
        self.DEX = self.makeField(4, 1, 2)
        self.CON = self.makeField(1, 1, 3)
        self.INT = self.makeField(0, 1, 4)
        self.WIS = self.makeField(1, 1, 5)
        self.CHA = self.makeField(1, 1, 6)
        self.ATK = self.makeField(5, 1, 8)
        self.AC  = self.makeField(18,1,10)


        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())
        #self.entry.focus_set()
        #self.entry.selection_range(0, Tkinter.END)

    def rollAttack1(self):     # MW composite longbow +2
        critRange = 20
        crit = 3
        dmgBase = [1, 8]                                                              # 1d8
        dmgBonus = 2 + self.raptorArrow + self.isPointBlank.get() + 2*(self.isFavored.get() or self.isPouch.get())          # +2 composite
        atkBase = [1,20]
        atkBonus = self.ATK.get() + self.DEX.get() + 1 + self.raptorArrow + self.isPointBlank.get() - 2*self.isRapidShot.get() + self.isPouch.get()    # MW
        atkField = self.atk1result
        dmgField = self.dmg1result
        commentField = self.comment1
        
        self.attack(atkBase, atkBonus, dmgBase, dmgBonus, critRange, crit, atkField, dmgField, commentField)

    def rollAttack2(self):    # MW Longsword
        critRange = 19
        crit = 2
        dmgBase = [1, 8]  
        dmgBonus = self.STR.get() + 2 * (self.isFavored.get() or self.isPouch.get())
        atkBase = [1,20]               
        atkBonus = self.ATK.get() + self.STR.get() + 2*(self.isFlanking.get() + self.isCharging.get()) + 1 - 2 + self.isPouch.get()      # MW and noncombatant
        atkField = self.atk2result
        dmgField = self.dmg2result
        commentField = self.comment2

        self.attack(atkBase, atkBonus, dmgBase, dmgBonus, critRange, crit, atkField, dmgField, commentField)

    def rollAttack3(self):      # Shortsword
        critRange = 19
        crit = 2
        dmgBase = [1, 6]  
        dmgBonus = self.STR.get() + 2 * (self.isFavored.get() or self.isPouch.get())
        atkBase = [1,20]               
        atkBonus = self.ATK.get() + self.STR.get() + 2*(self.isFlanking.get() + self.isCharging.get()) - 2 + self.isPouch.get()           # noncombatant
        atkField = self.atk3result
        dmgField = self.dmg3result
        commentField = self.comment3

        self.attack(atkBase, atkBonus, dmgBase, dmgBonus, critRange, crit, atkField, dmgField, commentField)


    def attack(self, atkBase, atkBonus, dmgBase, dmgBonus, critRange, crit, atkField, dmgField, commentField):
        rolldie  = self.roll(atkBase)
        if rolldie == 1:                                                       # if natural 1
            rolldie2 = self.roll(atkBase)
            if rolldie2 == 1:                                                     # if another natural 1
                rolldie3 = self.roll(atkBase)
                atkroll = rolldie3 + atkBonus
                atkField.set(atkroll)
                dmgField.set(0)
                commentField.set('Snake Eyes!! (1, 1, %d)' % rolldie3)
            else:
                atkroll = rolldie2 + atkBonus
                atkField.set(atkroll)
                dmgField.set(0)
                commentField.set('Natural One!! (1, %d)' % rolldie2)
        elif rolldie >= critRange:                                             # if critical
            rolldie2 = self.roll(atkBase)
            if rolldie == 20 and rolldie2 == 20:                                             # if two natural 20's
                rolldie3 = self.roll(atkBase)
                atkroll = rolldie3 + atkBonus
                atkField.set(atkroll)
                dmgField.set( [self.roll([crit*dmgBase[0],dmgBase[1]]) + crit * dmgBonus,  'Dead'] )
                commentField.set('Double Crit!! (%d, %d, %d)' % (rolldie, rolldie2, rolldie3) )
            else:
                atkroll = rolldie2 + atkBonus
                atkField.set(atkroll)
                dmgField.set( [self.roll(dmgBase) + dmgBonus, self.roll([crit*dmgBase[0],dmgBase[1]]) + crit * dmgBonus] )
                commentField.set('Crit!! (%d, %d)' % (rolldie, rolldie2) )
        else:                                                                  # Otherwise, normal roll
            atkField.set(rolldie + atkBonus)
            dmgField.set( self.roll(dmgBase) + dmgBonus )
            commentField.set('Natural roll: %d' % rolldie)

if __name__ == "__main__":
    app = roll(None)
    app.title('Belkul Moonshadow')
    app.mainloop()

