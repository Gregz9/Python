import test_world 
import pynput 
from pynput.keyboard import Listener 
from pynput.keyboard import Key, Controller

class Sheep(): 
    def __init__(self, picture, pos_left, pos_top):
        self._picture = picture
        self._pos_left = pos_left
        self._pos_top = pos_top
        self._speed_from_left = 2 
        self._speed_from_top = 2 
        
 

    def move_left(self): 
        if(self._pos_left == test_world.WIDTH): 
            self._pos_left = 0
        else: 
            self._pos_left += self._speed_from_left
    
    def move_right(self) :
        if(self._pos_left == 0): 
            self._pos_left = test_world.WIDTH
        else: 
            self._pos_left += self._speed_from_left 
    
    def move_up(self):
        if(self._pos_top == 0): 
            self._pos_top = test_world.HEIGHT
        else: 
            self._pos_top -= self._speed_from_top
    
    def move_down(self): 
        if(self._pos_top == test_world.HEIGHT): 
            self._pos_top = 0 
        else: 
            self._pos_top += self._speed_from_top


    
    def draw(self, screen): 
        screen.blit(self._picture, (self._pos_left, self._pos_top)) 

    
    

