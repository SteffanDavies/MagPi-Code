# GEOMETRIC SHAPES
# By Jaseman - 10th May 2012

import os, pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

pygame.display.set_caption("Geometric Shapes")
screen = pygame.display.set_mode([400, 200], 0, 32)

# Draw a CIRCLE on screen in (red) at (x, y) coords (60, 70) of diameter 40
pygame.draw.circle(screen, (255, 0, 0), (60, 70), 40)

pygame.display.update()
pygame.time.wait(2000)

# Draw a RECTANGLE on the screen in (yellow) at (x, y, width, height)
pygame.draw.rect(screen, (255, 255, 0), (70, 70, 120, 60))

pygame.display.update()
pygame.time.wait(2000)

# Draw a LINE on the screen in (blue) from (x,y), (x,y), (width)
pygame.draw.line(screen, (0, 0, 255), (10, 150), (370, 30), 10)

pygame.display.update()
pygame.time.wait(10000)
