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

        self.setMinimumSize(QSize(300, 120))
        self.setCentralWidget(self.stackedWidget)

        self.setWindowTitle("Minesweeper")


    def showMainMenu(self):
        self.stackedWidget.setCurrentIndex(0)

    def showSettingsMenu(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def showGameScreen(self):
        self.stackedWidget.setCurrentIndex(2)

    def getAreaSize(self):
        return self.settingsMenu.getAreaSize()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
