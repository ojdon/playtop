import pygame

import xdg.Menu
import xdg.DesktopEntry


class PlaytopMenu:

    def __init__(self):
        self.show_menu(xdg.Menu.parse())

    def show_menu(self, menu, depth=0):
        for entry in menu.getEntries():
            if isinstance(entry, xdg.Menu.Menu):
                menu.show_menu(entry, depth)
            elif isinstance(entry, xdg.Menu.MenuEntry):
                print(menu.getPath() + "/	" + entry.DesktopFileID + "	" + entry.DesktopEntry.getFileName())




