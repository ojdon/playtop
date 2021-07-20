import fontawesome as fa
import pygame
import psutil


class Battery:
    def __init__(self, ws, x, y, col=(255, 255, 255)):
        self.status = fa.icons['battery-empty']
        self.ws = ws
        self.x = x
        self.y = y
        self.col = col

        self.get_status()

    def get_status(self):
        battery = psutil.sensors_battery()

        if battery.power_plugged:
            self.status = fa.icons['bolt']
        elif battery.percent > 90:
            self.status = fa.icons['battery-full']
        elif battery.percent > 75:
            self.status = fa.icons['battery-three-quarters']
        elif battery.percent > 50:
            self.status = fa.icons['battery-half']
        elif battery.percent > 25:
            self.status = fa.icons['battery-quarter']
        else:
            self.col = (255, 0, 0)

    def update(self):
        self.get_status()

    def draw(self):
        # Set up the text
        basic_font = pygame.font.Font("./assets/fonts/fontawesome-solid.otf", 24)

        text = basic_font.render(self.status, True, self.col)
        text_rect = text.get_rect()
        text_rect.centerx = self.x
        text_rect.centery = self.y

        # Draw the text onto the surface
        self.ws.blit(text, text_rect)
