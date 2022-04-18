from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLCDNumber
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

        self.mineCounter = QLCDNumber()
        self.mineCounter.setDecMode()
        restartBox.addWidget(self.mineCounter)

        self.restartButton = QPushButton(":)")
        self.restartButton.clicked.connect(self.init_game_area)
        restartBox.addWidget(self.restartButton)

        self.widgetLayout = QVBoxLayout()        
        self.widgetLayout.addLayout(self.titleHBox)
        self.widgetLayout.addLayout(restartBox)

        self.game_area = GameArea(self.window.getAreaSize(), self.window.getNumberOfMines(), parent=self)
        self.game_area.gameEnded.connect(self.game_end)
        self.mineCounter.display(len(self.game_area.grid))
        self.game_area.markedCell.connect(self.mineCounterSlot)

        self.widgetLayout.addWidget(self.game_area)

        self.setLayout(self.widgetLayout)

    def init_game_area(self):
        self.restartButton.setText(":)")
        self.game_area.setParent(None)
        self.game_area = GameArea(self.window.getAreaSize(), self.window.getNumberOfMines(), parent=self)
        self.game_area.gameEnded.connect(self.game_end)
        self.game_area.markedCell.connect(self.mineCounterSlot)
        self.mineCounter.display(len(self.game_area.grid))
        self.widgetLayout.addWidget(self.game_area)

    def generate_new_schema(self):
        self.game_area.generate_new_schema()
        self.mineCounter.display(len(self.game_area.grid))

    def game_end(self):
        self.restartButton.setText(":(")

    def mineCounterSlot(self, diff):
        self.mineCounter.display(self.mineCounter.value() + diff)