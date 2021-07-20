import pygame
from .widgets.battery import Battery
from .widgets.clock import Clock


class Taskbar:
    def __init__(self, ws, col, w, h):
        self.ws = ws
        self.col = col
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(self.ws, self.col, pygame.Rect(0, 0, self.w, self.h))
        battery_icon = Battery(self.ws, self.w - 24, self.h / 2)
        battery_icon.draw()

        clock = Clock(self.ws, self.w / 2 , self.h / 2)
        clock.draw()
