#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor
from random import randint

from constVocation import LIST_VOCATION
from constEthn import LIST_ETHNIE

""" Class Personnage """

class Personnage():

    # Constructor
    def __init__(self, c_name, id_vocation, id_ethn, **kwargs):
        
        #Check parameters
        self.checkID_Vocation(id_vocation)
        self.checkID_Ethn(id_ethn)
        

        # Parameters for user input for character creation
        self.c_name = c_name
        self.id_vocation = id_vocation
        self.id_ethn = id_ethn

        # Optionnal parameters
        self.lvl = kwargs.get("lvl") if kwargs.get("lvl") != None else 1
        self.exp = kwargs.get("exp") if kwargs.get("exp") != None else 1

        self.max_pv = kwargs.get("max_pv") if kwargs.get("max_pv") != None else 10
        self.cur_pv = kwargs.get("cur_pv") if kwargs.get("cur_pv") != None else 10

        self.att_phy = kwargs.get("att_phy") if kwargs.get("att_phy") != None else 10
        self.def_phy = kwargs.get("def_phy") if kwargs.get("def_phy") != None else 10
        self.att_spe = kwargs.get("att_spe") if kwargs.get("att_spe") != None else 10
        self.def_spe = kwargs.get("def_spe") if kwargs.get("def_spe") != None else 10
        self.vit = kwargs.get("vit") if kwargs.get("vit") != None else 10

        self.id_itemTete = kwargs.get("id_itemTete") if kwargs.get("id_itemTete") != None else 0
        self.id_itemTorse = kwargs.get("id_itemTorse") if kwargs.get("id_itemTorse") != None else 0
        self.id_itemJambe = kwargs.get("id_itemJambe") if kwargs.get("id_itemJambe") != None else 0
        self.id_itemBotte = kwargs.get("id_itemBotte") if kwargs.get("id_itemBotte") != None else 0
        self.id_itemArme = kwargs.get("id_itemArme") if kwargs.get("id_itemArme") != None else 0
        self.id_itemBonus = kwargs.get("id_itemBonus") if kwargs.get("id_itemBonus") != None else 0
        self.bag = kwargs.get("bag") if kwargs.get("bag") != None else [[1,1]]

    # Save the character into the database
    def saveCharacter(self):
        return None
    
    # Load the character from the database
    def loadCharacter(self):
        return None
    
    # Show character current characters data in a readable way
    def showCharacter(self):
        print("Character name : " + self.c_name)
        print("Vocation : " + LIST_VOCATION[self.id_vocation]['Name'])
        print("Ethnie : " + LIST_ETHNIE[self.id_ethn]['Name'])

        print("PV : " + str(self.cur_pv))
        print("ATT : " + str(self.att_phy))
        print("DEF : " + str(self.def_phy))
        print("ATTSPE : " + str(self.att_spe))
        print("DEFSPE : " + str(self.def_spe))
        print("VIT : " + str(self.vit))

    # Show character bag contents in a readable way
    def showBag(self):
        return None

    # Show character currently equipped weapon/armor in a readable way
    def showStuff(self):
        return None

    #
    def checkID_Vocation(self, id_vocation):
        if (id_vocation > -1 and id_vocation < len(LIST_VOCATION)):
            return id_vocation
        else:
            raise ValueError('Invalid id_vocation')

    def checkID_Ethn(self, id_ethn):
        if (id_ethn > -1 and id_ethn < len(LIST_ETHNIE)):
            return id_ethn
        else:
            raise ValueError('Invalid id_ethn')

    def damageCharacter(self, damageAmount):
        current_pv = current_pv = self.c_cur_pv - damageAmount
        if (current_pv <= 0):
            self.c_cur_pv = 0
        else:
            self.c_cur_pv = self.c_cur_pv - damageAmount

    def healCharacter(self, healAmount):
        current_pv = self.c_cur_pv + healAmount
        if (current_pv >= self.c_max_pv):
            self.c_cur_pv = self.c_max_pv
        else:
            self.c_cur_pv = current_pv

    def addItemToBag(self, idItem):
        return None

    def equipItem(self, idItem):
        return None

    def unequipItem(self, idItem):
        return None

    def addEXP(self, idItem):
        return None








# Tests
params = {
    "lvl": 5,
    "bag": [[1,12],[34,1]]
}

test = Personnage("Michel", 1, 3)
test.showCharacter()
print(test.bag)