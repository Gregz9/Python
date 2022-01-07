import pygame 
import os
import sys


WIDTH = 900
HEIGHT = 700

WHITE = (255, 255, 255)

pygame.init()
#creating a test screen
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
#creating the canvas
game_canvas = screen.copy()
game_canvas.fill(WHITE)
#drawing the canvas onto screen with coords 50, 50 (tho its using the upper left of game_canvas)
screen.blit(pygame.transform.scale(game_canvas, (200, 200)), (50, 50))
pygame.display.flip()

clock = pygame.time.Clock()
while True:
    delta_time = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()