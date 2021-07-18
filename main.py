import pygame, sys
from pygame.locals import *

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

#Set up the text
text = basicFont.render('HELLO WORLD', True, WHITE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#Draw the white background onto the surface
windowSurface.fill(BLUE)

#Draw the text onto the surface
windowSurface.blit(text,textRect)

#Set up taskbar
taskbar = Taskbar(windowSurface, BLACK, vw, 48)
taskbar.draw()

#Draw the window onto the screen
pygame.display.update()

#Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
