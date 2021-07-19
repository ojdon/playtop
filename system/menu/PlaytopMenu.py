import pygame

import xdg.Menu
import xdg.DesktopEntry


class PlaytopMenu:
    def show_menu(self, menu, depth=0):
        for entry in menu.getEntries():
            if isinstance(entry, xdg.Menu.Menu):
                self.show_menu(entry, depth)
            elif isinstance(entry, xdg.Menu.MenuEntry):
                print(menu.getPath() + "/	" + entry.DesktopFileID + "	" + entry.DesktopEntry.getFileName())

    def get_menu(self):
        return xdg.Menu.parse()



