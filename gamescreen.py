from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from gamearea import GameArea

class GameScreen(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.dimensions = window.getAreaSize()

        backButton = QPushButton("<-")
        backButton.setFixedSize(30, 30)
        backButton.clicked.connect(self.window.showMainMenu)

        gameScreenLabel = QLabel("Minesweeper")
        gameScreenLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.titleHBox = QHBoxLayout()
        self.titleHBox.addWidget(backButton)
        self.titleHBox.addWidget(gameScreenLabel)

        restartBox = QHBoxLayout()
        restartButton = QPushButton(":)")
        restartButton.clicked.connect(self.init_game_area)
        restartBox.addWidget(restartButton)

        self.widgetLayout = QVBoxLayout()        
        self.widgetLayout.addLayout(self.titleHBox)
        self.widgetLayout.addLayout(restartBox)

        self.game_area = GameArea(self.window.getAreaSize(), self.window.getNumberOfMines(), parent=self)

        self.widgetLayout.addWidget(self.game_area)

        self.setLayout(self.widgetLayout)

    def init_game_area(self):
        self.game_area.setParent(None)
        self.game_area = GameArea(self.window.getAreaSize(), self.window.getNumberOfMines(), parent=self)
        self.widgetLayout.addWidget(self.game_area)
