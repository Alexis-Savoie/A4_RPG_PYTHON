#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random

from constMob import LIST_MOB


""" Class Mob """

class Mob():

    # Constructor
    def __init__(self, mob_id):

        # Initialiez mob properties and stats
        self.mob_id = mob_id
        self.mob_name = LIST_MOB[mob_id]["name"]

        self.max_pv = LIST_MOB[mob_id]["pv"]
        self.cur_pv = self.max_pv

        self.att_phy = LIST_MOB[mob_id]["att_phy"]
        self.def_phy = LIST_MOB[mob_id]["def_phy"]
        self.att_spe = LIST_MOB[mob_id]["att_spe"]
        self.def_spe = LIST_MOB[mob_id]["def_spe"]
        self.vit = LIST_MOB[mob_id]["vit"]

        self.mob_exp = LIST_MOB[mob_id]["exp"]
        self.fuite = LIST_MOB[mob_id]["fuite"]
        self.drop_item_id = LIST_MOB[mob_id]["drop_item_id"]
        self.drop_prob = LIST_MOB[mob_id]["drop_prob"]


    def damageMob(self, damageAmount):
        current_pv = current_pv = self.cur_pv - damageAmount
        if (current_pv <= 0):
            self.cur_pv =  0
        else:
            self.cur_pv = self.cur_pv - damageAmount

    def healMob(self, healAmount):
        current_pv = self.cur_pv + healAmount
        if (current_pv >= self.mob_max_pv):
            self.cur_pv = self.mob_max_pv
        else:
            self.cur_pv = current_pv

    def mobLoot(self):
        random.randint(0, 100)
        if (self.drop_prob <= random.randint(0, 100)):
            return self.drop_item_id
        else:
            return False

test = Mob(0)
print(test.mob_name)