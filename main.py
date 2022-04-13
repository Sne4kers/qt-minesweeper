import sys

from mainmenuwidget import MainMenu
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow, QMenu, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        mainMenu = MainMenu()
        self.setCentralWidget(mainMenu)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop.
app.exec()
