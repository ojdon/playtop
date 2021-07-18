import pygame

class Taskbar: 
    def __init__(self, ws, col, w, h):
        self.ws = ws
        self.col = col
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(self.ws, self.col, pygame.Rect(0, 0, self.w, self.h))