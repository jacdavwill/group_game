# Name: Jacob Williams
# Date: 3/10/2015
# Subject: Class game
# File Name: Hero.py

import Person
import random

class Hero(Person.Person):
    health = 5
    cash = 5
    name = ""
    x_pos = 0
    y_pos = 0
    level = 1
    
    def __init__(self,name):
        self.name = name
        print("\nHello {0}. I am glad to see another adventurer in these parts.\n".format(name))
        print("Welcome to another game of Gold!!!")
        print("##########################################################")

    def set_level(self,level):
        self.level = level

    def left(self):
        if self.x_pos == 0:
            print("\nHey, you are on the edge of the map {0}. You cannot move left.".format(self.name))
            print("##########################################################")
        else:
            self.x_pos -= 1
            print("\nYou successfully moved to the left.\n")
            print("{0}, your new position is ({1} , {2}).".format(self.name,self.x_pos,self.y_pos))
            print("##########################################################")
            
    def right(self):
        if self.x_pos == self.level + 3:
            print("\nHey, you are on the edge of the map {0}. You cannot move right.".format(self.name))
            print("##########################################################")
        else:
            self.x_pos += 1
            print("\nYou successfully moved to the left.\n")
            print("{0}, your new position is ({1} , {2}).".format(self.name,self.x_pos,self.y_pos))
            print("##########################################################")

    def up(self):
        if self.y_pos == self.level + 3:
            print("\nHey, you are on the top of the map {0}. You cannot move up.".format(self.name))
            print("##########################################################")
        else:
            self.y_pos += 1
            print("\nYou successfully moved up.\n")
            print("{0}, your new position is ({1} , {2}).".format(self.name,self.x_pos,self.y_pos))
            print("##########################################################")

    def down(self):
        if self.y_pos == 0:
            print("\nHey, you are on the bottom of the map {0}. You cannot move down.".format(self.name))
            print("##########################################################")
        else:
            self.y_pos -= 1
            print("\nYou successfully moved down.\n")
            print("{0}, your new position is ({1} , {2}).".format(self.name,self.x_pos,self.y_pos))
            print("##########################################################")

    def find_gold(self):
        print("\nWow, you found the gold. It contains {0} coins.".format(str(self.level * 5)))
        print("##########################################################")
        
    def find_spike(self):
        print("\nOuch, you stepped on a spike. You lost 1 health")
        print("##########################################################")
        self.health -= 1
        
    def find_door(self):
        self.x_pos = 0
        self.y_pos = 0
        print("\nYikes, a trapdoor. You are transported to a random location.")
        print("##########################################################")
        
