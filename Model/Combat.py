#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint


from Mob import *
from Personnage import *

""" Class Mob """

class Combat():

    # Constructor
    def __init__(self, inputPersonnage: Personnage, inputMob: Mob):

        # Initialize Combat
        self.inputPersonnage = inputPersonnage
        self.inputMob = inputMob

        self.isFinished = False


    def playerMoveFirst(self):
        if (self.inputPersonnage >= self.inputMob):
            return True
        else:
            return False

    def lancerDe(self):
        return randint(0, 99)


    def calculateDamage(self, targetIsPlayer: bool, isPhysical: bool, resultat_de: int):
        #define target and if attack is special or not
        if (targetIsPlayer):
            attacker = self.inputMob
            target = self.inputPersonnage
        else:
            attacker = self.inputPersonnage
            target = self.inputMob

        if (isPhysical):
            attackStat = attacker.att_phy
            defenseStat = target.def_phy
        else:
            attackStat = attacker.att_spe
            defenseStat = target.def_spe

        #Définir le facteur du dé
        if (resultat_de >=0 and resultat_de <= 4):
            facteur_de = 0
        elif (resultat_de >=5 and resultat_de <= 25):
            facteur_de = 0.25
        elif (resultat_de >=26 and resultat_de <= 49):
            facteur_de = 0.5
        elif (resultat_de >=50 and resultat_de <= 74):
            facteur_de = 1
        elif (resultat_de >=75 and resultat_de <= 94):
            facteur_de = 2
        elif (resultat_de >=95 and resultat_de <= 99):
            facteur_de = 4


        damage = (((attackStat/defenseStat)/50)+2)*facteur_de 
        damage = round(damage, 0)
        return damage







# Tests

perso = Personnage("Michel", 1, 3)
mob = Mob(0)
combat = Combat(perso, mob)
rDe = combat.lancerDe()

print(combat.calculateDamage(True, True, rDe))