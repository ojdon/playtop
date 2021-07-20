from datetime import datetime

import pygame, sys
from pygame.locals import *
import json
import time

# TODO: Move this to a module
from system.menu.PlaytopMenu import PlaytopMenu

system_json = open('./data/json/system.json')
system_data = json.load(system_json)
system_json.close()

from system.taskbar.Taskbar import Taskbar

# Set up pygame
pygame.init()

pygame.display.set_caption('Playtop')
pygame.display.set_icon(pygame.image.load('./assets/img/icons/logo/logo-squared.png'))
clock = pygame.time.Clock()

# Set up the window
vw = pygame.display.Info().current_w
vh = pygame.display.Info().current_h

# windowSurface = pygame.display.set_mode((vw, vh), pygame.NOFRAME)
windowSurface = pygame.display.set_mode((vw, vh))

# Set up the colors
PRIMARY = system_data['palette']['primary']
DARK = system_data['palette']['dark']
LIGHT = system_data['palette']['light']

# Set up fonts
basic_font = pygame.font.SysFont(None, 48)

# Draw the background onto the surface
windowSurface.fill(DARK)

# Set up taskbar
taskbar = Taskbar(windowSurface, DARK, vw, 48)
menu = PlaytopMenu()

try:
    menu.show_menu(menu.get_menu())
except:
    menuError = basic_font.render("Error: Unable to load menu.", True, LIGHT)
    text_rect = menuError.get_rect()
    text_rect.centerx = vw / 2
    text_rect.centery = vh / 2

    # Draw the text onto the surface
    windowSurface.blit(menuError, text_rect)

loop = True


def update():
    taskbar.update()

def draw():
    taskbar.draw()

while loop:
    for event in pygame.event.get():
        if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
    # Update Screen.
    update()
    draw()

    pygame.display.flip()
    clock.tick(30)
