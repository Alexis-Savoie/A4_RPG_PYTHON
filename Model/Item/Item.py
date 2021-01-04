

from math import floor
from random import randint
from utils.const import LIST_ITEMS

""" Class Item """

class Item():

    def __init__(self, level, type_personnage):
        # Catact. d'un object
        self.attaque = 1
        self.defense = 1
        self.vitesse = 1
        self.chance = 1
        self.mana = 1
        self.vie = 1

        chance = randint(1, floor((level/2)+1)) # 1.{chance} * catégorie buff
        randItem = floor(randint(0, len(LIST_ITEMS)-1))
        
        self.name = self.get_name_by_key(randItem) # Objet name give
        self.objet = LIST_ITEMS[self.name] # Objet give

        if self.objet["catg"] == 1: # Si object de type attaque
            self.attaque = (1+(2 if type_personnage == self.objet['type_personnage'] else 1)/100)+chance/100
        elif self.objet["catg"] == 2:
            self.defense = (1+(2 if type_personnage == self.objet['type_personnage'] else 1)/100)+chance/100
        elif self.objet["catg"] == 3:
            self.vitesse = (1+(2 if type_personnage == self.objet['type_personnage'] else 1)/100)+chance/100
        elif self.objet["catg"] == 4:
            self.chance = (1+(2 if type_personnage == self.objet['type_personnage'] else 1)/100)+chance/100
        elif self.objet["catg"] == 5:
            self.mana = (1+(2 if type_personnage == self.objet['type_personnage'] else 1)/100)+chance/100
        elif self.objet["catg"] == 6:
            self.vie = (1+(2 if type_personnage == self.objet['type_personnage'] else 1)/100)+chance/100

    def get_name_by_key(self, n=0):
        if n < 0:
            n += len(LIST_ITEMS)
        for i, key in enumerate(LIST_ITEMS.keys()):
            if i == n:
                return key
        raise IndexError("dictionary index out of range")

    def __str__(self):
        return "Key:"+str(self.objet["key"])+"\n"+"Name:"+self.name+"\n"+"Type items:"+str(self.objet["catg"])+"\n"+"Attaque:"+str(self.attaque)+"\n"+"Defense:"+str(self.defense)+"\n"+"Vitesse:"+str(self.vitesse)+"\n"+"Chance:"+str(self.chance)+"\n"+"Mana:"+str(self.mana)+"\n"+"Vie:"+str(self.vie)+"\n"

# Test module
if __name__ == "__main__":
    level = 50
    item = Item(level, 1) 
    print('Mon level est: '+str(level))
    print(item)