import space_world
import space_ship 
import math 
import random


class LottaBoss: 
    def __init__(self, picture, pos_left, pos_top, num_lives): 
        self._picture = picture
        self._pos_left = pos_left
        self._pos_top = pos_top
        self._num_lives = num_lives
        self._direction = 1 
        self._alive = True
        self._num_hits = math.inf


    def alive(self): 
        return self._alive

    def move(self): 

        direction = random.randint(0, 4)

        if(du): 
            

