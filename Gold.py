#Filename: GOLD
#Author: Spandan Timilsina
#Date: 3/10/15
#Purpose: create a class for gold earned per level
import Person

class Gold(Person.Person):
    inventory = []

    def Purchase(item):
        global gold
        global inventory

        price = store[item]

        if gold >= price:
            gold -= price
            inventory.append(item)
        else:
            print ("You can't purchase this.")
