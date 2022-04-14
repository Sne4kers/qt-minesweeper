from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout

class GameArea(QWidget):
    def __init__(self, gridSize, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = gridSize[0]
        self.height = gridSize[1]
        gridButtonLayout = QGridLayout()
        for i in range(self.height):
            for j in range(self.width):
                button = QPushButton(parent=self)
                gridButtonLayout.addWidget(button, i, j)
        self.setLayout(gridButtonLayout)