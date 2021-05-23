# OPEN A PYGAME GRAPHICS WINDOW
# By Jaseman - 03 May 2012

import os, pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

# This title appears along the top of the graphics window
pygame.display.set_caption("The Title Of My Program")

# Opens a graphics window called 'screen' with width 400 height 200
screen = pygame.display.set_mode([400, 200], 0, 32)

pygame.time.wait(5000) # A 5 second pause before ending the program
