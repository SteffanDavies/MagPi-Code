# THREE SURFACES
# By Jaseman - 13th June 2012

import os, pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Three Surfaces")
screen = pygame.display.set_mode([400, 200], 0, 32) # The main screen

sky = pygame.Surface((400, 200)) # A sky surface
sky.fill((200, 255, 255)) # Fill the surface in light blue color
grass = pygame.Surface((400, 100)) # A grass surface
grass.fill((50, 150, 50)) # Fill the surface in green color
sun = pygame.Surface((40, 40)) # A sun surface
pygame.draw.circle(sun, (255, 255, 0), (20, 20), 20)
screen.blit(sky, (0, 0)) # Paste the sky surface at x, y
screen.blit(sun, (180, 30)) # Paste the sun surface at x, y
screen.blit(grass, (0, 100)) # Paste the grass surface at x, y

pygame.display.update()
pygame.time.wait(10000) # A 10 second pause before ending the program