from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpinBox, QPushButton
from PyQt6.QtCore import Qt

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

        titleHBox = QHBoxLayout()
        titleHBox.addWidget(backButton)
        titleHBox.addWidget(gameScreenLabel)

        layout = QVBoxLayout()
        layout.addLayout(titleHBox)

        self.setLayout(layout)