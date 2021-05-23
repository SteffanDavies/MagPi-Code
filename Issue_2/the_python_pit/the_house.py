# THE HOUSE
# By 0the0judge0 - 29th of May 2012

import os, pygame;
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
d = pygame.draw # this will save us writing 'pygame.draw' many times

pygame.display.set_caption("The House")

# Define some colors
white = (255, 255, 255); black = (0, 0, 0)
bg = (186, 213, 48); walls = (157, 109, 9)
door = (151, 36, 9); door_light = (181, 132, 14)

# coordinates of glass panes
windows = [(82, 125), (82, 215), (262, 125), (262, 215)]

# init screen
screen = pygame.display.set_mode([423, 347], 0, 32)

# the walls
screen.fill(bg) # fill the background screen colour
d.rect(screen, black, (60, 102, 305, 225))
d.rect(screen, walls, (73, 114, 280, 200))

# the roof
d.polygon(screen, black, ((35, 112), (121, 12), (296, 12), (321, 36), (321, 12), (361, 12), (361, 84), (384, 112)))
d.polygon(screen, walls, ((62, 101), (128, 23), (289, 23), (334, 69), (334, 25), (348, 25), (348, 88), (361, 101)))

# the door
d.rect(screen, black, (167, 198, 84, 125))
d.rect(screen, door, (179, 210, 60, 101 ))
d.rect(screen, black, (185, 216, 50, 54 ))
d.rect(screen, black, (191, 222, 38, 41 ))
d.circle(screen, black, (209, 277), 5)

# the windows 
for window in windows:
	d.rect(screen, black, (window[0], window[1], 76, 76))
	d.rect(screen, black, (window[0] + 12, window[1] + 12, 22, 22)) # tl
	d.rect(screen, black, (window[0] + 42, window[1] + 12, 22, 22)) # tr
	d.rect(screen, black, (window[0] + 12, window[1] + 42, 22, 22)) # bl
	d.rect(screen, black, (window[0] + 42, window[1] + 42, 22, 22)) # br

# let's see the end result
pygame.display.update()
pygame.time.wait(10000)
pygame.quit()