import pygame

import xdg.Menu
import xdg.DesktopEntry


class PlaytopMenu:
    def __init__(self):
        pass

    def show_menu(self, menu, depth=0):
        menu_list = {}

        for entry in menu.getEntries():
            if isinstance(entry, xdg.Menu.Menu):
                self.show_menu(entry, depth)
            elif isinstance(entry, xdg.Menu.MenuEntry):
                # print(menu.getPath() + "/	" + entry.DesktopFileID + "	" + entry.DesktopEntry.getFileName())
                item = {"name": entry.DesktopEntry.getName(), "icon": entry.DesktopEntry.getIcon()}
                menu_list.update(item)
                print(menu_list)

        return menu_list

    def get_menu(self):
        return xdg.Menu.parse()
