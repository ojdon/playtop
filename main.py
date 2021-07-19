import pygame, sys
from pygame.locals import *

from system.menu.Menu import Menu
from system.taskbar.Taskbar import Taskbar

#Set up pygame
pygame.init()

#Set up the window
vw = pygame.display.Info().current_w
vh = pygame.display.Info().current_h

# windowSurface = pygame.display.set_mode((vw, vh), pygame.NOFRAME)
windowSurface = pygame.display.set_mode((vw, vh))

pygame.display.set_caption('Playtop')

#Set up the colors
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

#Set up fonts
basicFont = pygame.font.SysFont(None, 48)

#Draw the white background onto the surface
windowSurface.fill(BLUE)

#Set up taskbar
taskbar = Taskbar(windowSurface, BLACK, vw, 48)
taskbar.draw()

menu = Menu()

#Draw the window onto the screen
pygame.display.update()

#Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
