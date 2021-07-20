import pygame
import time


class Clock:
    def __init__(self, ws, x, y, col=(255, 255, 255)):
        self.ws = ws
        self.x = x
        self.y = y
        self.col = col

    def draw(self):
        # Set up the text
        basic_font = pygame.font.SysFont(None, 24)

        text = basic_font.render(time.strftime("%H:%M"), True, self.col)
        text_rect = text.get_rect()
        text_rect.centerx = self.x
        text_rect.centery = self.y

        # Draw the text onto the surface
        self.ws.blit(text, text_rect)
