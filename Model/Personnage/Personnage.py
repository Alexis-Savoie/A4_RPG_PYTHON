#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor
from random import randint
from utils.const import TYPE_ETHNIE

""" Class Personnage """
class Personne():
    def __init__(self):
        self.email = ''
        self.password = ''

class Personnage(Personne):

    # Constructor
    def __init__(self, name, type_personnage, ethnie, sexe):
        super().__init__()
        self.name = name # Nom
        self.type_personnage = type_personnage # - Guerrier => 1 - Voleur => 2 - Mage => 3
        self.ethnie = ethnie # "Congo": 1, "Mongolie": 2, "France": 3, "USA": 4, "Japon": 5, "Cote_Ivoire": 6, "Argentine": 7, "Haiti": 8, "Angleterre": 9
        self.sexe = sexe # - Homme - Femmme - Trans
        self.attaque = 0
        self.defense = 0
        self.vitesse = 0
        self.chance = 0
        self.mana = 0
        self.vie = 10
        self.exp = 0
        self.level = 1
        self.stock = []
        self.stuff = { # index du stock
            "Attaque":-1,
            "Defense":-1,
            "Vitesse":-1,
            "Mana":-1,
            "Chance":-1,
            "Vie":-1,
        }
        self.init()

    def init(self):
        if self.name == 'Mike':
            self.attaque = 2
            self.defense = 2
            self.vitesse = 2
            self.chance = 2
            self.mana = 2
            self.vie = 2
            self.exp = 2

        """ Stats type personnage """

        if(self.type_personnage == 1): # - Guerrier
            self.attaque += randint(15, 20)
            self.defense += randint(15, 20)
            self.vitesse += randint(5, 10)
            self.chance += randint(10, 15)
            self.mana += randint(5, 10)
            self.vie += randint(10, 15)

            """ Stats type ethnie """
            if( 1 >= TYPE_ETHNIE.get(self.ethnie, 3) <= 3): # "Congo": 1, "Mongolie": 2, "France": 3
                choix = randint(0, 1)
                if choix: # Si true Defense BUFF & Mana NERF
                    self.defense *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                    self.mana /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else: # Si false Attaque BUFF & Vitesse NERF
                    self.attaque *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                    self.vitesse /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)

            """ Stats sexe """
            if self.sexe == 1:
                choix = randint(0, 1) # BUFF
                if choix:
                    self.defense *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else:
                    self.attaque *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                choix = randint(0, 1) # NERF
                if choix:
                    self.mana /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else:
                    self.vitesse /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)






        elif(self.type_personnage == 2): # - Voleur
            self.attaque += randint(10, 15)
            self.defense += randint(5, 10)
            self.vitesse += randint(15, 20)
            self.chance += randint(15, 20)
            self.mana += randint(10, 15)
            self.vie += randint(5, 10)

            """ Stats type ethnie """
            if( 4 >= TYPE_ETHNIE.get(self.ethnie, 3) <= 6): # "USA": 4, "Japon": 5, "Cote_Ivoire": 6
                choix = randint(0, 1)
                if choix: # Si true vitesse BUFF & defense NERF
                    self.vitesse *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                    self.defense /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else: # Si false chance BUFF & vie NERF
                    self.chance *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                    self.vie /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)

            """ Stats sexe """
            if self.sexe == 1:
                choix = randint(0, 1) # BUFF
                if choix:
                    self.vitesse *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else:
                    self.chance *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                choix = randint(0, 1) # NERF
                if choix:
                    self.defense /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else:
                    self.vie /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)


        elif(self.type_personnage == 3):
            self.attaque += randint(5, 10)
            self.defense += randint(10, 15)
            self.vitesse += randint(10, 15)
            self.chance += randint(5, 10)
            self.mana += randint(15, 20)
            self.vie += randint(15, 20)

            """ Stats type ethnie """
            if( 7 >= TYPE_ETHNIE.get(self.ethnie, 3) <= 9): # "Argentine": 7, "Haiti": 8, "Angleterre": 9
                choix = randint(0, 1)
                if choix: # Si true mana BUFF & attaque NERF
                    self.mana *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                    self.attaque /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else: # Si false vie BUFF & chance NERF
                    self.vie *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                    self.chance /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)

            """ Stats sexe """
            if self.sexe == 1:
                choix = randint(0, 1) # BUFF
                if choix:
                    self.mana *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else:
                    self.vie *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                choix = randint(0, 1) # NERF
                if choix:
                    self.attaque /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else:
                    self.chance /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
        
        self.attaque = floor(self.attaque)
        self.defense = floor(self.defense)
        self.vitesse = floor(self.vitesse)
        self.chance = floor(self.chance)
        self.mana = floor(self.mana)
        self.vie = floor(self.vie)


    def add_item_to_stock(self, item):
        self.stock.append(item)

    def liste_inventaire_du_stock(self):
        print('*********************** Inventaire ***********************')
        for item in self.stock:
            print("Key:"+str(item.objet["key"])+"\n")
            print("Name:"+item.name+"\n")
            print("Type items:"+str(item.objet["catg"])+"\n")
            print('-------------- Caract. --------------')
            print("Attaque:"+str(item.attaque)+"\n")
            print("Defense:"+str(item.defense)+"\n")
            print("Vitesse:"+str(item.vitesse)+"\n")
            print("Chance:"+str(item.chance)+"\n")
            print("Mana:"+str(item.mana)+"\n")
            print("Vie:"+str(item.vie)+"\n")
        print('*********************** END ***********************')


    def __str__(self):
        self.liste_inventaire_du_stock()
        return "attaque: " + str(self.attaque)+"\n"+ "defense: " + str(self.defense)+"\n"+ "vitesse: " + str(self.vitesse)+"\n"+ "chance: " + str(self.chance)+"\n"+ "mana: " + str(self.mana)+"\n"+ "vie: " + str(self.vie)+"\n"+ "stock: " + str(len(self.stock))+"\n"

if __name__ == "__main__":
    test = Personnage('Mike', 1, 'France', 1)
    print(test)
    test.liste_inventaire_du_stock()