# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 13:20:53 2023

@author: balar
"""
import os
import time
import pygame
time_elapsed = 10
keys = [False, False, False, False]
back_ground = [58,59,45,42,25]
back = 0

active_indexs = []
active_indexs2 = []

def make_sprite_list():
    sprite_list = os.listdir('Sprite')
    return sprite_list    
def make_sprite(img_num, x=0,y=0,rev_scalex = 1,rev_scaley = 1):
    imp = pygame.image.load('Sprite\\'+sprite_list[img_num]).convert_alpha()
    work_aroundx = DEFAULT_IMG_SZ[0]*rev_scalex
    work_aroundy= DEFAULT_IMG_SZ[1]*rev_scaley
    work_around = (work_aroundx,work_aroundy)
    imp = pygame.transform.scale(imp,work_around)
    screen.blit(imp, (x, y))
    return imp
class rev :
    def  __init__ (self,img,coin):
        self.image = img
        self.health = 100
        self.coin = coin
        self.food = 100
        self.water = 100
        self.time = time.time()
        self.space_time = 0

    def health_func (self):
        
        if(self.health > 0):
            if(self.water <=0):
                self.health -= 10
            if(self.food <= 0):
                self.health -= 10
            return self.health
   
    def add_food(self,food_added= 0,water_added = 0):
        self.food = 100
        
        self.change_time_s()
       
     
    def pet(self):
        if(self.health<100):
            self.health+=10
        self.change_time_s()
    def add_water(self,food_added= 0,water_added = 0):
        self.water = 100
        self.change_time_s()
    def food_water(self):
       new_time = time.time()
       change_time = new_time - self.time
       change_time2 = new_time - self.space_time
       try:
           if(change_time2 > 2):
                active_indexs2.pop()
          
       except:
           print(None)
       try:
            if(change_time > 5):
                for i in active_indexs:
                    active_indexs.pop()
                
       except:
            print(None)
       if(self.water> 0 and self.food > 0):
            if(change_time >= time_elapsed):
                food_ticks  = change_time // time_elapsed
                self.food -= food_ticks *10
                self.water -= food_ticks*2*10
                self.time += time_elapsed * food_ticks
       elif(self.food>0):
            if(change_time >= time_elapsed):
                food_ticks  = change_time // time_elapsed
                self.food -= food_ticks *10
                self.time += time_elapsed * food_ticks
                for num in range(0,int(food_ticks)):
                    self.health_func()
       elif(self.water>0):
            if(change_time >= time_elapsed):
                food_ticks  = change_time // time_elapsed
                self.water -= food_ticks *10
                self.time += time_elapsed * food_ticks * 2
                for num in range(0,int(food_ticks)):
                    self.health_func()
       else:
            if( change_time >= 30):
                for num in range(0,int(change_time//(time_elapsed/2))):
                    self.health_func()  
                    self.time += (time_elapsed/2)
            
       
       print(change_time2)


    def change_time_s (self):
        self.time = time.time()

# Get the current processor
# time in seconds
game = True
my_rev  = rev('hi',500)
DEFAULT_IMG_SZ = (1920*.8,1290*.8)

pygame.init()
screen = pygame.display.set_mode((1920*.8, 1280*.8))
clock = pygame.time.Clock()
running = True
sprite_list = make_sprite_list()
imp  = make_sprite(12)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   #food bar 
    if(my_rev.health== 100):
       make_sprite(11)
    if(my_rev.food== 90):
        make_sprite(8)
    if(my_rev.food == 80):
        make_sprite(7)
    if(my_rev.food == 70):
        make_sprite(6)
    if(my_rev.food == 60):
        make_sprite(5)
    if(my_rev.food == 50):
        make_sprite(4)
    if(my_rev.food == 40):
        make_sprite(3)
    if(my_rev.food == 30):
        make_sprite(2)
    if(my_rev.food == 20):
        make_sprite(1)
    if(my_rev.food == 10):
       make_sprite(0)
    if(my_rev.food == 0):
       make_sprite(10)
    #water bar
    if(my_rev.health== 100):
        make_sprite(57)
    if(my_rev.water== 90):
        make_sprite(54)
    if(my_rev.water == 80):
        make_sprite(53)
    if(my_rev.water == 70):
        make_sprite(52)
    if(my_rev.water == 60):
        make_sprite(51)
    if(my_rev.water == 50):
        make_sprite(52)
    if(my_rev.water == 40):
        make_sprite(51)
    if(my_rev.water == 30):
        make_sprite(50)
    if(my_rev.water == 20):
        make_sprite(49)
    if(my_rev.water == 10):
       make_sprite(48)
    if(my_rev.water == 0):
       make_sprite(56)
    #health
    if(my_rev.health== 100):
        make_sprite(24)
    if(my_rev.health== 90):
        make_sprite(22)
    if(my_rev.health == 80):
        make_sprite(21)
    if(my_rev.health == 70):
        make_sprite(20)
    if(my_rev.health == 60):
        make_sprite(19)
    if(my_rev.health == 50):
        make_sprite(18)
    if(my_rev.health == 40):
        make_sprite(17)
    if(my_rev.health == 30):
        make_sprite(16)
    if(my_rev.health == 20):
        make_sprite(15)
    if(my_rev.health == 10):
       make_sprite(14)
    if(my_rev.health == 0):
       make_sprite(23)
    #rev
    print('time ',time.time())
    
    if event.type == pygame.KEYUP:
        if event.key==pygame.K_a:
            keys[0]=False
            my_rev.add_food()
            
            if 9 not in active_indexs:
                active_indexs.append(9)
        elif event.key==pygame.K_t:
            keys[1]=False
            my_rev.pet()

            if 37 not in active_indexs:
                active_indexs.append(37)
        elif event.key==pygame.K_m:
            keys[2]=False
            my_rev.add_water()
            if 55 not in active_indexs:
                active_indexs.append(55)
        elif event.key==pygame.K_b:
             
            print(event.key)
            if back < len(back_ground)-1:
                back+=1
            else:
                back = 0
        elif event.key==pygame.K_SPACE:
             
            if 61 not in active_indexs2:
                active_indexs2.append(61)
                my_rev.space_time = time.time()
    event.key = pygame.K_i

    
    make_sprite(back_ground[back],300-80+10+10+5-5,140-20-10+10+10,2/3,.5)
    make_sprite(13,300-80+10+10-10+10,140-20+1-1+10,2/3,.5)
    if(my_rev.water < 31 or my_rev.food < 31):
        make_sprite(41,300-80+10+10-10+10,140-20+1-1+10,2/3,.5)

    for i in active_indexs:
        make_sprite(i,300-80+10+10+5-5,140-20-10+10+10,2/3,.5)
    for j in active_indexs2:
        print(len(active_indexs2))
        make_sprite(j)
        
    if(my_rev.health == 0):
        make_sprite(62)
        
    # fill the screen with a color to wipe away anything from last frame
    my_rev.food_water()
    print('rev food', my_rev.water)
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
 
# print the current
# processor time
