import sys

from mainmenuwidget import MainMenu
from settingswidget import SettingsMenu
from gamescreen import GameScreen
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow, QMenu, QVBoxLayout, QMessageBox, QStackedWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainMenu = MainMenu(self)
        self.settingsMenu = SettingsMenu(self)
        self.gameScreen = GameScreen(self)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.addWidget(self.mainMenu)
        self.stackedWidget.addWidget(self.settingsMenu)
        self.stackedWidget.addWidget(self.gameScreen)

        self.setCentralWidget(self.stackedWidget)
        self.showMainMenu()
        self.setWindowTitle("Minesweeper")


    def showMainMenu(self):
        self.setFixedSize(QSize(self.getAreaSize()[0]*25 + 50, self.getAreaSize()[1]*25 + 50))
        self.stackedWidget.setCurrentIndex(0)

    def showSettingsMenu(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def showGameScreen(self):
        self.gameScreen.init_game_area()
        self.stackedWidget.setCurrentIndex(2)

    def getAreaSize(self):
        return self.settingsMenu.getAreaSize()

    def getNumberOfMines(self):
        return self.settingsMenu.getNumberOfMines()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
