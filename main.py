import sys

from mainmenuwidget import MainMenu
from settingswidget import SettingsMenu
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow, QMenu, QVBoxLayout, QMessageBox, QStackedWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainMenu = MainMenu(self)
        self.settingsMenu = SettingsMenu(self)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.addWidget(self.mainMenu)
        self.stackedWidget.addWidget(self.settingsMenu)

        self.setMinimumSize(QSize(300, 120))
        self.setCentralWidget(self.stackedWidget)


    def showMainMenu(self):
        self.setWindowTitle("Menu")
        self.stackedWidget.setCurrentIndex(0)

    def showSettingsMenu(self):
        self.setWindowTitle("Settings")
        self.stackedWidget.setCurrentIndex(1)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
