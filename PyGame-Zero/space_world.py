#from monster import Monster 

from game import Game 
import os 
import pygame

WIDTH = 900
HEIGHT = 800

game = Game() 

pygame.init()

def draw(): 
   
    pygame.display.set_caption('Somewhere in space')
    game.draw(screen)

def update():
    game.update(keyboard)



