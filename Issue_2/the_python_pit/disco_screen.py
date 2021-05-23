# DISCO SCREEN
# By Jaseman - 10th May 2012

import os, pygame
from pygame.locals import * 

pygame.init()

clock = pygame.time.Clock;

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

pygame.display.set_caption("Disco Screen")

screen = pygame.display.set_mode([400, 200], 0, 32)

screen.fill((255, 0, 0))
pygame.display.update() 
pygame.time.wait(2000)

screen.fill((255, 255, 0))
pygame.display.update() 
pygame.time.wait(2000)

screen.fill((0, 255, 0))
pygame.display.update() 
pygame.time.wait(2000)

screen.fill((0, 0, 255))
pygame.display.update() 
pygame.time.wait(2000)

screen.fill((0, 255, 255))
pygame.display.update() 
pygame.time.wait(2000)

screen.fill((255, 0, 255))
pygame.display.update() 
pygame.time.wait(2000)

screen.fill((255, 255, 255))
pygame.display.update() 
pygame.time.wait(2000)

screen.fill((0, 0, 0))
pygame.display.update() 
pygame.time.wait(2000)