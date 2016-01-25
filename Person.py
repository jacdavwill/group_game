#Filename: PERSON
#Author: Spandan Timilsina
#Date: 3/10/15
#Purpose: create a class for Person

import random

class Person:
    def set_image(self,image):
        self.image = image

    def get_image(self):
        return self.image
    
    def get_pos(self,level):
        xPos2 = random.randint (0, level + 3)
        yPos2 = random.randint (0, level + 3)

        while (xPos2 == level + 3 and yPos2 == level + 3) or (xPos2 == 0 and yPos2 == 0) or (xPos2 == level + 3 and yPos2 == level + 2):
            xPos2 = random.randint (0, level + 3)
            yPos2 = random.randint (0, level + 3)

        self.x_pos = xPos2
        self.y_pos = yPos2
