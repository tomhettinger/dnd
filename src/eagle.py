#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import random

class eagle(Tkinter.Tk):

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
        self.makeAtk("Talons", 2, 1, self.talons)
        self.makeAtk("Talons", 2, 3, self.talons2)
        self.makeAtk("Bite",   2, 5, self.bite)
        self.makeAtk("Full Attack", 2, 7, self.fullAtk)
        self.makeAtk("Go Attack", 2, 8, self.goAttack)
        self.isFlanking = self.makeCheck("is Flanking", 3, 9)
        self.isCharging = self.makeCheck("is Charging", 4, 9)

        # Roll results
        self.makeLabel("Attack Roll",          3, 0, 1,10)
        self.atk1result = self.makeField(0, 3, 1)
        self.atk2result = self.makeField(0, 3, 3)
        self.atk3result = self.makeField(0, 3, 5)
        self.atk4result = self.makeField(0, 3, 8)

        # Damage Done
        self.makeLabel("Dmg on Hit",           4, 0, 1,10)
        self.dmg1result = self.makeField(0, 4, 1)
        self.dmg2result = self.makeField(0, 4, 3)
        self.dmg3result = self.makeField(0, 4, 5)

        # Comments
        self.comment1 = self.makeLabel("Ready to Attack", 5, 1, 1, 25, 'red')
        self.comment2 = self.makeLabel("Ready to Attack", 5, 3, 1, 25, 'red')
        self.comment3 = self.makeLabel("Ready to Attack", 5, 5, 1, 25, 'red')
        self.comment4 = self.makeLabel("Ready to Attack", 5, 8, 1, 25, 'red')

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
        self.HP  = self.makeField(8, 1, 0)
        self.STR = self.makeField(0, 1, 1)
        self.DEX = self.makeField(2, 1, 2)
        self.CON = self.makeField(1, 1, 3)
        self.INT = self.makeField(-4,1, 4)
        self.WIS = self.makeField(2, 1, 5)
        self.CHA = self.makeField(-2,1, 6)
        self.ATK = self.makeField(0, 1, 8)
        self.AC  = self.makeField(14,1,10)


        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())

    def fullAtk(self):
        self.talons()
        self.talons2()
        self.bite()

    def talons(self):     
        critRange = 20
        crit = 2
        dmgBase = [1, 4]                                                              # 1d8
        dmgBonus = self.DEX.get()
        atkBase = [1,20]
        atkBonus = self.ATK.get() + self.STR.get() + 3 + 2*(self.isFlanking.get() + self.isCharging.get())
        atkField = self.atk1result
        dmgField = self.dmg1result
        commentField = self.comment1
        
        self.attack(atkBase, atkBonus, dmgBase, dmgBonus, critRange, crit, atkField, dmgField, commentField)

    def talons2(self):     
        critRange = 20
        crit = 2
        dmgBase = [1, 4]                                                              # 1d8
        dmgBonus = self.DEX.get()
        atkBase = [1,20]
        atkBonus = self.ATK.get() + self.STR.get() + 3 + 2*(self.isFlanking.get() + self.isCharging.get())
        atkField = self.atk2result
        dmgField = self.dmg2result
        commentField = self.comment2
        
        self.attack(atkBase, atkBonus, dmgBase, dmgBonus, critRange, crit, atkField, dmgField, commentField)

    def bite(self):
        critRange = 20
        crit = 2
        dmgBase = [1, 4]  
        dmgBonus = self.DEX.get()
        atkBase = [1,20]               
        atkBonus = self.ATK.get() + self.STR.get() - 2 + 2*(self.isFlanking.get() + self.isCharging.get())
        atkField = self.atk3result
        dmgField = self.dmg3result
        commentField = self.comment3

        self.attack(atkBase, atkBonus, dmgBase, dmgBonus, critRange, crit, atkField, dmgField, commentField)

    def goAttack(self):
        rolldie = self.roll([1, 20])
        handleBonus = 7
        handleDC = 10
        atkResult = rolldie + handleBonus
        self.atk4result.set(atkResult)
        if atkResult >= handleDC:
            self.comment4.set("DC: %d  Success!  Nat:%d" % (handleDC, rolldie))
        else:
            self.comment4.set("DC: %d  Fail!  Nat:%d" % (handleDC, rolldie))


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
    app = eagle(None)
    app.title('Tobias')
    app.mainloop()

