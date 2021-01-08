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
        self.checkID_Ethn(id_vocation)

        # Parameters for user input for character creation
        self.c_name = c_name
        self.id_vocation = id_vocation
        self.id_ethn = id_ethn

        # OPtionnal parameters
        self.lvl = kwargs.get("lvl") if kwargs.get("lvl") != None else 1
        self.exp = kwargs.get("exp") if kwargs.get("exp") != None else 1

        self.c_hp = kwargs.get("c_hp") if kwargs.get("c_hp") != None else 10
        self.c_att = kwargs.get("c_att") if kwargs.get("c_att") != None else 10
        self.c_def = kwargs.get("c_def") if kwargs.get("c_def") != None else 10
        self.c_att_spe = kwargs.get("c_att_spe") if kwargs.get("c_att_spe") != None else 10
        self.c_def_spe = kwargs.get("c_def_spe") if kwargs.get("c_def_spe") != None else 10
        self.c_vit = kwargs.get("c_vit") if kwargs.get("c_vit") != None else 10

        self.id_itemTete = kwargs.get("id_itemTete") if kwargs.get("id_itemTete") != None else 0
        self.id_itemTorse = kwargs.get("id_itemTorse") if kwargs.get("id_itemTorse") != None else 0
        self.id_itemJambe = kwargs.get("id_itemJambe") if kwargs.get("id_itemJambe") != None else 0
        self.id_itemBotte = kwargs.get("id_itemBotte") if kwargs.get("id_itemBotte") != None else 0
        self.id_itemArme = kwargs.get("id_itemArme") if kwargs.get("id_itemArme") != None else 0
        self.id_itemBonus = kwargs.get("id_itemBonus") if kwargs.get("id_itemBonus") != None else 0
        self.bag = kwargs.get("bag") if kwargs.get("bag") != None else [[1,1]]

    def showCharacter(self):
        print("Character name : " + self.c_name)
        print("Vocation : " + LIST_VOCATION[self.id_vocation]['Name'])
        print("Ethnie : " + LIST_ETHNIE[self.id_ethn]['Name'])

        print("PV : " + str(self.c_hp))
        print("ATT : " + str(self.c_att))
        print("DEF : " + str(self.c_def))
        print("ATTSPE : " + str(self.c_att_spe))
        print("DEFSPE : " + str(self.c_def_spe))
        print("VIT : " + str(self.c_vit))


    def showBag(self):
        return None

    def showStuff(self):
        return None

    def checkID_Vocation(self, id_vocation):
        return None

    def checkID_Ethn(self, id_ethn):
        if (id_ethn > -1 and id_ethn < len(LIST_ETHNIE)):
            return id_ethn
        else:
            raise ValueError('Invalid id_ethn')

    def damageCharacter(self, damageAmount):
        return None

    def healCharacter(self, healAmount):
        return None

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