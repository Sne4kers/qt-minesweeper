from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt, QSize

class GameArea(QWidget):
    def __init__(self, gridSize, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = gridSize[0]
        self.height = gridSize[1]
        gridButtonLayout = QGridLayout()
        gridButtonLayout.setSpacing(0)
        for i in range(self.height):
            for j in range(self.width):
                button = QPushButton(parent=self)
                button.setMinimumSize(QSize(10,10))
                button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
                gridButtonLayout.addWidget(button, i, j)
        self.setLayout(gridButtonLayout)