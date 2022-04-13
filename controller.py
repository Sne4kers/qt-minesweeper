from mainmenuwidget import MainMenu
from settingswidget import SettingsMenu
from PyQt6.QtWidgets import QMainWindow

class Controller():
    def __init__(self, window):
        self.window = window
        self.mainMenu = MainMenu(self)
        self.settingsMenu = SettingsMenu(self)
    
    def showMainMenu(self):
        self.window.setCentralWidget(self.mainMenu)

    def showSettingsMenu(self):
        print("Tried to launch settings")
        self.window.setCentralWidget(self.settingsMenu)

    def printDebug(self):
        print("Debugging with style!")