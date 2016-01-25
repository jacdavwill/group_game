# Name: Jacob Williams
# Date: 3/12/15
# Purpose: pygame for class game
# Filename: classpygame_pygame.py

import pygame
import sys
import math
import Person
import Hero
import Spike
import Door
import Gold
import time

#initialization
pygame.init()
name = input("Hello. What is your name? ")

screen_w = 750
screen_h = 750
size = [screen_w, screen_h]

screen = pygame.display.set_mode(size)

h = Hero.Hero(name)
d = Door.Door()
s = Spike.Spike()
g = Gold.Gold()

door_image = pygame.image.load("door.png")
door_rect = door_image.get_rect()
d.set_image(door_image)

spike_image = pygame.image.load("spike.png")
spike_rect = spike_image.get_rect()
s.set_image(spike_image)

gold_image = pygame.image.load("gold.png")
gold_rect = gold_image.get_rect()
g.set_image(gold_image)

hero_image = pygame.image.load("hero.png")
hero_rect = hero_image.get_rect()
h.set_image(hero_image)

heart_image = pygame.image.load("heart.png")
heart_rect = heart_image.get_rect()

dollar_image = pygame.image.load("dollar.png")
dollar_rect = dollar_image.get_rect()

h.set_level(1)

spike_rect.x = 55
gold_rect.x = 110

heart_rect.x = 680
heart_rect.y = 400
dollar_rect.x = 680
dollar_rect.y = 555

# colors
black = (0, 0, 0)
blue = (5,5,255)
red = (255,5,5)
yellow = (255,255,0)
pink = (255, 92, 205)
green = (0,255,0)
turq = (81,242,236)

# banners
life = h.health
life_str = "LIFE"
life_str_num = str(life)
cash = h.cash
cash_str = "CASH"
cash_str_num = str(cash)
level_str = "LEVEL  " + str(h.level)
save = "Press S to save game"
load = "Press L to load game"
new_game = "Game Loading..."
save_game = "Game Saving..."
death_str = "You have failed"
try_again = "Try again(y/n): "
shop_str = "Buy health?"
shop = 0
money = 0
hero_cash = "Hero's cash: " + str(h.cash)
hero_health = "Hero's health: " + str(h.health)
cost_str = "Cost: "
instructions = "Press ENTER when done"

stat_font = pygame.font.Font(None,75)
banner_font = pygame.font.Font(None,100)
save_font = pygame.font.Font(None,50)

new_game_str = banner_font.render(new_game, 1, green)
save_game_str = banner_font.render(save_game, 1, green)
life_stat = stat_font.render(life_str, 1, pink)
cash_stat = stat_font.render(cash_str, 1, yellow)
banner = banner_font.render(level_str, 1, red)
life_str_num_stat = stat_font.render(life_str_num, 1, pink)
cash_str_num_stat = stat_font.render(cash_str_num, 1, yellow)
save_str = save_font.render(save, 1, red)
load_str = save_font.render(load, 1, red)
death_str_stat = banner_font.render(death_str, 1, red)
try_again_stat = banner_font.render(try_again, 1, green)
shop_str_stat = banner_font.render(shop_str, 1, turq)
shop_num_stat = banner_font.render(str(shop), 1, red)
money_num_stat = banner_font.render(str(money), 1, yellow)
hero_cash_str = banner_font.render(hero_cash, 1, yellow)
hero_health_str = banner_font.render(hero_health, 1, pink)
cost_str_stat = stat_font.render(cost_str, 1, yellow)
instructions_str = stat_font.render(instructions, 1, green)

life_size = stat_font.size(life_str)
cash_size = stat_font.size(cash_str)
banner_size = banner_font.size(level_str)

# grid
class Grid():
    level = 1
    delta = 1
    
    def __init__(self,x,y,screen_h,level):
        self.x = x
        self.h = screen_h
        self.level = level
        self.delta = 502.5 / (level + 4)
        
        self.y = y

    def get_pos(self):
        return [[30 + self.delta * self.x,self.h - 30 - self.delta * self.y],[30 + self.delta * (self.x + 1),self.h - 30 - self.delta * self.y],[30 + self.delta * (self.x + 1),self.h - 30 - self.delta * (self.y + 1)],[30 + self.delta * self.x,self.h - 30 - self.delta * (self.y + 1)],False]

def create_grid(screen_h,level):
    grid = []
   
    for y in range(level + 4):

        for x in range(level + 4):
            a = Grid(x,y,screen_h,level)
            grid.append(a.get_pos())
            
    grid[0][4] = True
    grid[-1][4] = True
    
    return grid

spike_list = []
spike_rects = []
all_spikes = []

door_list = []
door_rects = []
all_doors = []

positions = []

def image_pos(x, y, level, h, delta):
    return [30 + delta * x,h - 30 - delta * (y + 1)]

def create_spikes(level,positions):
    spike_pos = positions
    for x in range(level * 3):
        a = Spike.Spike()
        a.set_image(spike_image)
        a.get_pos(level)
        pos_list = [a.x_pos,a.y_pos]
        
        while pos_list in spike_pos:
            a.get_pos(level)
            pos_list = [a.x_pos,a.y_pos]
            
        spike_list.append(a)
        spike_pos.append([a.x_pos,a.y_pos])
        all_spikes.append([a.x_pos,a.y_pos])

def create_doors(level,positions):
    door_pos = positions
    for x in range(level):
        a = Door.Door()
        a.set_image(door_image)
        a.get_pos(level)
        pos_list = [a.x_pos,a.y_pos]
        
        while pos_list in door_pos:
            a.get_pos(level)
            pos_list = [a.x_pos,a.y_pos]
            
        door_list.append(a)
        door_pos.append([a.x_pos,a.y_pos])
        all_doors.append([a.x_pos,a.y_pos])

def save_game(cash, health, level):
    f = open("class_game.txt","w")
    f.write(str(cash) + "\n")
    f.write(str(health) + "\n")
    f.write(str(level) + "\n")
    for item in all_spikes:
        for num in item:
            f.write(str(num) + " ")

    f.close()

def load_game():
    f = open("class_game.txt","r")
    ans = f.readlines()
    h.cash = int(ans[0].strip())
    h.health = int(ans[1].strip())
    h.level = int(ans[2].strip())

create_spikes(h.level,positions)
create_doors(h.level,positions)

grid = create_grid(screen_h,h.level)

delta = 502.5 / (h.level + 4)

def set_items():
    
    for spike in spike_list:
        rect = spike.get_image().get_rect()
        rect.x = image_pos(spike.x_pos,spike.y_pos,h.level,screen_h, delta)[0]
        rect.y = image_pos(spike.x_pos,spike.y_pos,h.level,screen_h, delta)[1]
        spike_rects.append(rect)

    for door in door_list:
        rect = door.get_image().get_rect()
        rect.x = image_pos(door.x_pos,door.y_pos,h.level,screen_h, delta)[0]
        rect.y = image_pos(door.x_pos,door.y_pos,h.level,screen_h, delta)[1]
        door_rects.append(rect)

def go_shopping():
    done = False
    shop = 0
    money = 0
    while not done:
        shop_num_stat = banner_font.render(str(shop), 1, red)
        money_num_stat = banner_font.render(str(money), 1, yellow)
        hero_cash = "Hero's cash: " + str(h.cash)
        hero_health = "Hero's health: " + str(h.health)
    
        hero_cash_str = save_font.render(hero_cash, 1, yellow)
        hero_health_str = save_font.render(hero_health, 1, pink)
        
        heart_rect.x = 585
        heart_rect.y = 305
        dollar_rect.x = 175
        dollar_rect.y = 305
        
        screen.fill(black)
        screen.blit(instructions_str,(65,700))
        screen.blit(cost_str_stat, (30,305))
        screen.blit(hero_cash_str, (60,500))
        screen.blit(hero_health_str, (400,500))
        screen.blit(money_num_stat, (230, 300))
        screen.blit(shop_str_stat, (200,200))
        screen.blit(shop_num_stat, (500,300))
        screen.blit(pygame.transform.scale(heart_image,(50,50)), heart_rect)
        screen.blit(pygame.transform.scale(dollar_image,(50,50)), dollar_rect)
        pygame.display.flip()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if pygame.key.get_pressed()[pygame.K_UP]:
                if h.cash >= money + 2:
                    shop += 1
                    money += 2

            if pygame.key.get_pressed()[pygame.K_DOWN]:
                if shop > 0:
                    shop -= 1
                    money -= 2

            if pygame.key.get_pressed()[pygame.K_RETURN]:
                h.cash -= money
                h.health += shop
                done = True

                
    h.cash += h.level + 4
    h.level += 1
    h.x_pos = 0
    h.y_pos = 0

set_items()
shop = 0
money = 0

##### game loop ######################################
while True:
    heart_rect.x = 680
    heart_rect.y = 400
    dollar_rect.x = 680
    dollar_rect.y = 555
    
    delta = 502.5 / (h.level + 4)
    life = h.health
    life_str_num = str(life)
    life_str_num_stat = stat_font.render(life_str_num, 1, pink)
    cash = h.cash
    cash_str_num = str(cash)
    cash_str_num_stat = stat_font.render(cash_str_num, 1, yellow)
    level_str = "LEVEL  " + str(h.level)
    banner = banner_font.render(level_str, 1, red)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if pygame.key.get_pressed()[pygame.K_s]:
            save_game(h.cash,h.health,h.level)
            print("Your game is saved\n")
            screen.fill(black)
            screen.blit(save_game_str, (100, 350))
            pygame.display.flip()
            time.sleep(1)
            

        if pygame.key.get_pressed()[pygame.K_l]:
            load_game()
            print("Your previous game is loaded\n")
            screen.fill(black)
            screen.blit(new_game_str, (100, 350))
            pygame.display.flip()
            
            h.x_pos = 0
            h.y_pos = 0
            grid = create_grid(screen_h,h.level)
            delta = 502.5 / (h.level + 4)
            positions = []
            spike_list = []
            spike_rects = []
            all_spikes = []

            door_list = []
            door_rects = []
            all_doors = []
            create_spikes(h.level,positions)
            create_doors(h.level,positions)
            time.sleep(1)
            
            set_items()

        if pygame.key.get_pressed()[pygame.K_UP]:
            h.up()
            grid[h.y_pos * (h.level + 4) + h.x_pos][4] = True
            pos = [h.x_pos,h.y_pos]
            if pos in all_spikes:
                h.find_spike()
            if pos in all_doors:
                h.find_door()
            if pos == [h.level + 3,h.level + 3]:
                h.find_gold()
                
                # start shopping
                go_shopping()

                grid = create_grid(screen_h,h.level)
                delta = 502.5 / (h.level + 4)
                positions = []
                spike_list = []
                spike_rects = []
                all_spikes = []

                door_list = []
                door_rects = []
                all_doors = []
                create_spikes(h.level,positions)
                create_doors(h.level,positions)
                
                set_items()
                    
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            h.right()
            grid[h.y_pos * (h.level + 4) + h.x_pos][4] = True
            pos = [h.x_pos,h.y_pos]
            if pos in all_spikes:
                h.find_spike()
            if pos in all_doors:
                h.find_door()
            if pos == [h.level + 3,h.level + 3]:
                h.find_gold()
                
                # start shopping
                go_shopping()
                
                grid = create_grid(screen_h,h.level)
                delta = 502.5 / (h.level + 4)
                positions = []
                spike_list = []
                spike_rects = []
                all_spikes = []

                door_list = []
                door_rects = []
                all_doors = []
                create_spikes(h.level,positions)
                create_doors(h.level,positions)
                
                set_items()
                
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            h.down()
            grid[h.y_pos * (h.level + 4) + h.x_pos][4] = True
            pos = [h.x_pos,h.y_pos]
            if pos in all_spikes:
                h.find_spike()
            if pos in all_doors:
                h.find_door()
            
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            h.left()
            grid[h.y_pos * (h.level + 4) + h.x_pos][4] = True
            pos = [h.x_pos,h.y_pos]
            if pos in all_spikes:
                h.find_spike()
            if pos in all_doors:
                h.find_door()

        # player dies
        if h.health <= 0:
            print("\nYou have died\n")
            screen.fill(black)
            screen.blit(death_str_stat, (100,200))
            screen.blit(try_again_stat, (100,300))
            pygame.display.flip()
            
            done = False
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if pygame.key.get_pressed()[pygame.K_y]:
                        done = True
                        h.health = 5
                        h.cash = 5
                        h.level = 1
                        h.x_pos = 0
                        h.y_pos = 0
                        grid = create_grid(screen_h,h.level)
                        delta = 502.5 / (h.level + 4)
                        positions = []
                        spike_list = []
                        spike_rects = []
                        all_spikes = []

                        door_list = []
                        door_rects = []
                        all_doors = []
                        create_spikes(h.level,positions)
                        create_doors(h.level,positions)
                    
                        set_items()
                            
                    if pygame.key.get_pressed()[pygame.K_n]:
                        pygame.quit()
                        sys.exit()
                        
    # screen display
    screen.fill(black)

    ## banners
    screen.blit(banner, (227,59))
    screen.blit(life_stat, (601,320))
    pygame.draw.polygon(screen, pink, [[582,382],[582,392],[730,392],[730,382]], 0)
    screen.blit(cash_stat, (582,484))
    pygame.draw.polygon(screen, yellow, [[582,154 + 382],[582,154 + 392],[730,154 + 392],[730,154 + 382]], 0)
    screen.blit(life_str_num_stat,(580,400))
    screen.blit(cash_str_num_stat,(580,555))
    screen.blit(save_str,(0,0))
    screen.blit(load_str,(400,0))

    ### pictures
    gold_rect.x = image_pos(h.level + 3,h.level + 3,h.level,screen_h, delta)[0]
    gold_rect.y = image_pos(h.level + 3,h.level + 3,h.level,screen_h, delta)[1] + 2
    hero_rect.x = image_pos(h.x_pos,h.y_pos,h.level,screen_h, delta)[0]
    hero_rect.y = image_pos(h.x_pos,h.y_pos,h.level,screen_h, delta)[1]
    
    for num in range(len(spike_list)):
        s = spike_list[num]
        if grid[(s.y_pos * (h.level + 4)) + s.x_pos][4]:
            screen.blit(pygame.transform.scale(spike_list[num].get_image(), (int(delta),int(delta))), spike_rects[num])

    for num in range(len(door_list)):
        d = door_list[num]
        if grid[(d.y_pos * (h.level + 4)) + d.x_pos][4]:
            screen.blit(pygame.transform.scale(door_list[num].get_image(), (int(delta),int(delta))), door_rects[num])
    
    # draw grid
    pygame.draw.polygon(screen, green,[[30,screen_h - 30],[502.5 + 30, screen_h - 30],[502.5 + 30, screen_h - 502.5 - 30],[30, screen_h - 502.5 - 30]], 5)
    
    for item in grid:
        if item[4] == True:
            pygame.draw.polygon(screen, green, item, 5)
        
    screen.blit(pygame.transform.scale(g.image, (int(delta),int(delta))), gold_rect)
    screen.blit(pygame.transform.scale(h.image, (int(delta),int(delta))), hero_rect)
    screen.blit(pygame.transform.scale(heart_image,(50,50)), heart_rect)
    screen.blit(pygame.transform.scale(dollar_image,(50,50)), dollar_rect)
    
    pygame.display.flip()
