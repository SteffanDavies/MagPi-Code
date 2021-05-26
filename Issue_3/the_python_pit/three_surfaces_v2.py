# THREE SURFACES V2
# By Jaseman - 13th June 2012

import os, pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Three Surfaces")
screen = pygame.display.set_mode([400, 200], 0, 32) # The main screen

sky = pygame.Surface((400, 200)) # A sky surface
sky.fill((200, 255, 255)) # Fill the surface in a light blue color
grass = pygame.Surface((400, 100)) # A grass surface
grass.fill((50, 150, 50)) # Fill the surface in a green color
sun = pygame.Surface((80, 80)) # A sun surface
sun.set_colorkey([0, 0, 0])
sun.set_alpha(128)
pygame.draw.circle(sun, (255, 255, 0), (40, 40), 40)
pygame.draw.circle(sun, (0, 0, 0), (40, 40), 15)

while True: # A never ending loop to keep the program running
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		mousex, mousey = pygame.mouse.get_pos()
		screen.blit(sky, (0, 0)) # Paste the sky surface at x,y
		screen.blit(grass, (0,100)) # Paste the surface at x,y
		screen.blit(sun, (mousex, mousey)) # Paste the sun surface at x,y

		pygame.display.update()