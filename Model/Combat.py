#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


from Mob import *
from Personnage import *

from constMob import LIST_MOB

""" Class Mob """

class Combat():

    # Constructor
    def __init__(self, inputPersonnage: Personnage, inputMob: Mob):

        # Initialize Combat
        self.inputPersonnage = inputPersonnage
        self.inputMob = inputMob

        self.isFinished = False
        self.fightEndedWith = None


    def playerMoveFirst(self):
        if (self.inputPersonnage.vit >= self.inputMob.vit):
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


        damage = ((50*(attackStat/defenseStat)/50)+2)*facteur_de 
        damage = round(damage, 0)
        return damage


    def PlayerUsePhysicalAttack(self):
        returnArr = []
        texteAttaqueEnnemie = [" attaque (physique) ", " attaque (spéciale) "]
        #User attacks first
        if (self.playerMoveFirst() == True):
            resultat_de = self.lancerDe()
            mobDamage = self.calculateDamage(False, True, resultat_de)
            self.inputMob.damageMob(mobDamage)
            returnArr.append(self.inputPersonnage.c_name + " attaque (physique) " + str(resultat_de) + "! " + str(mobDamage) + " dégats infligé à " + self.inputMob.mob_name)
            if (self.inputMob.cur_pv < 1):
                self.isFinished = True
                self.fightEndedWith = "win"
            else:
                resultat_de = self.lancerDe()
                attaqueEnnemie = random.randint(0, 1)
                playerDamage = self.calculateDamage(True, attaqueEnnemie, resultat_de)
                self.inputPersonnage.damageCharacter(playerDamage)
                returnArr.append(self.inputMob.mob_name + texteAttaqueEnnemie[attaqueEnnemie] + str(resultat_de) + "! " + str(playerDamage) + " dégats infligé à " + self.inputPersonnage.c_name)
                if (self.inputPersonnage.cur_pv < 1):
                    self.isFinished = True
                    self.fightEndedWith = "lose"
        # User attacks in second
        else:
            resultat_de = self.lancerDe()
            attaqueEnnemie = random.randint(0, 1)
            playerDamage = self.calculateDamage(True, attaqueEnnemie, resultat_de)
            self.inputPersonnage.damageCharacter(playerDamage)
            returnArr.append(self.inputMob.mob_name + texteAttaqueEnnemie[attaqueEnnemie] + str(resultat_de) + "! " + str(playerDamage) + " dégats infligé à " + self.inputPersonnage.c_name)
            if (self.inputPersonnage.cur_pv < 1):
                self.isFinished = True
                self.fightEndedWith = "lose"
            else:
                resultat_de2 = self.lancerDe()
                mobDamage2 = self.calculateDamage(False, True, resultat_de2)
                self.inputMob.damageMob(mobDamage2)
                returnArr.append(self.inputPersonnage.c_name + " attaque (physique) " + str(resultat_de) + "! " + str(mobDamage) + " dégats infligé à " + self.inputMob.mob_name)
                if (self.inputMob.cur_pv < 1):
                    self.isFinished = True
                    self.fightEndedWith = "win"
        return returnArr



    def PlayerUseSpecialAttack(self):
        returnArr = []
        texteAttaqueEnnemie = [" attaque (physique) ", " attaque (spéciale) "]
        #User attacks first
        if (self.playerMoveFirst() == True):
            resultat_de = self.lancerDe()
            mobDamage = self.calculateDamage(False, False, resultat_de)
            self.inputMob.damageMob(mobDamage)
            returnArr.append(self.inputPersonnage.c_name + " attaque (spéciale) " + str(resultat_de) + "! " + str(mobDamage) + " dégats infligé à " + self.inputMob.mob_name)
            if (self.inputMob.cur_pv < 1):
                self.isFinished = True
                self.fightEndedWith = "win"
            else:
                resultat_de = self.lancerDe()
                attaqueEnnemie = random.randint(0, 1)
                playerDamage = self.calculateDamage(True, attaqueEnnemie, resultat_de)
                self.inputPersonnage.damageCharacter(playerDamage)
                returnArr.append(self.inputMob.mob_name + texteAttaqueEnnemie[attaqueEnnemie] + str(resultat_de) + "! " + str(playerDamage) + " dégats infligé à " + self.inputPersonnage.c_name)
                if (self.inputPersonnage.cur_pv < 1):
                    self.isFinished = True
                    self.fightEndedWith = "lose"
        # User attacks in second
        else:
            resultat_de = self.lancerDe()
            attaqueEnnemie = random.randint(0, 1)
            playerDamage = self.calculateDamage(True, attaqueEnnemie, resultat_de)
            self.inputPersonnage.damageCharacter(playerDamage)
            returnArr.append(self.inputMob.mob_name + texteAttaqueEnnemie[attaqueEnnemie] + str(resultat_de) + "! " + str(playerDamage) + " dégats infligé à " + self.inputPersonnage.c_name)
            if (self.inputPersonnage.cur_pv < 1):
                self.isFinished = True
                self.fightEndedWith = "lose"
            else:
                resultat_de2 = self.lancerDe()
                mobDamage2 = self.calculateDamage(False, False, resultat_de2)
                self.inputMob.damageMob(mobDamage2)
                returnArr.append(self.inputPersonnage.c_name + " attaque (spéciale) " + str(resultat_de) + "! " + str(mobDamage) + " dégats infligé à " + self.inputMob.mob_name)
                if (self.inputMob.cur_pv < 1):
                    self.isFinished = True
                    self.fightEndedWith = "win"
        return returnArr



    def PlayerTryToFlee(self):
        returnArr = []
        resultat_de = random.randint(0, 100)
        # Fuite réussite
        if (resultat_de >= 50):
            self.isFinished = True
            self.fightEndedWith = "flee"
        # Fuite raté (tour gaché et mob attaque)
        else:
            texteAttaqueEnnemie = [" attaque (physique) ", " attaque (spéciale) "]
            returnArr.append("Vous n'avez pas réussit à fuir...")
            resultat_de = self.lancerDe()
            attaqueEnnemie = random.randint(0, 1)
            playerDamage = self.calculateDamage(True, True, resultat_de)
            self.inputPersonnage.damageCharacter(playerDamage)
            returnArr.append(self.inputMob.mob_name + texteAttaqueEnnemie[attaqueEnnemie] + str(resultat_de) + "! " + str(playerDamage) + " dégats infligé à " + self.inputPersonnage.c_name)
            if (self.inputPersonnage.cur_pv < 1):
                self.isFinished = True
                self.fightEndedWith = "lose"
        return returnArr




# Tests

perso = Personnage("Michel", 1, 3)
mob = Mob(0)
perso.showBag()

combat = Combat(perso, mob)
while combat.isFinished == False:
    print("COMBAT :")
    print(perso.c_name + " : " + str(perso.cur_pv) + " PV")
    print(mob.mob_name + " : " + str(mob.cur_pv) + " PV")
    choix = input()
    if (choix == "f"):
        returnArr = combat.PlayerTryToFlee()
        print(returnArr)
        if (combat.fightEndedWith == "flee"):
            print("Vous prenez la fuite")
        if (combat.fightEndedWith == "lose"):
            print("DEFAITE ! vous avez perdu :c ")
    elif (choix == "o"):
        perso.removeItem(34, 1)
        perso.healCharacter(20)
        print("Vous utiliser Potion 20 pv restoré !")

    else:
        returnArr = combat.PlayerUsePhysicalAttack()
        print(returnArr)
        if (combat.fightEndedWith == "win"):
            print("VICTOIRE ! vous remporter " + str(mob.mob_exp) + " EXP")
            isLevelUp = perso.addEXP(mob.mob_exp)
            if (isLevelUp):
                print("Vous passez au niveau " + str(perso.lvl) + " !!!")
            loot = mob.mobLoot()
            if (loot != False):
                print(mob.mob_name + " a fait tomber l'objet " + LIST_ITEM[loot]['item_name'])
                perso.addItemToBag(loot, 1)
                perso.showBag()
        if (combat.fightEndedWith == "lose"):
            print("DEFAITE ! vous avez perdu :c ")

        


#print(combat.calculateDamage(True, True, rDe))