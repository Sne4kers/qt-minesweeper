from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt, QSize
import random

class GameArea(QWidget):
    def __init__(self, gridSize, numberMines, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid = {}
        self.width = gridSize[0]
        self.height = gridSize[1]
        self.clicked = {}
        self.gridButtonLayout = QGridLayout()
        self.gridButtonLayout.setSpacing(0)
        for i in range(self.height):
            for j in range(self.width):
                button = QPushButton(parent=self)
                button.setMinimumSize(QSize(20, 20))
                button.setMaximumSize(QSize(30, 30))
                button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
                button.clicked.connect(lambda ch, j=j, i=i: self.button_clicked(i, j))
                self.gridButtonLayout.addWidget(button, i, j)
        self.setLayout(self.gridButtonLayout)

        print("Number of generated mines: ", numberMines)
        for i in range(numberMines):
            xRandomMine = random.randint(0, self.width)
            yRandomMine = random.randint(0, self.height)
            while (yRandomMine, xRandomMine) in self.grid:
                xRandomMine = random.randint(0, self.width)
                yRandomMine = random.randint(0, self.height)
            self.grid[(yRandomMine, xRandomMine)] = -1

    def button_clicked(self, i, j):
        print("Clicked ", i, j)
        self.clicked[(i, j)] = True
        if i < 0 or j < 0 or i >= self.height or j >= self.width:
            return
        pressedButton = self.gridButtonLayout.itemAtPosition(i, j).widget()
        if (i, j) in self.grid:
            self.fail()
            pressedButton.setText("B")
        else:
            count = 0
            if (i + 1, j) in self.grid:
                count += 1
            if (i - 1, j) in self.grid:
                count += 1
            if (i, j - 1) in self.grid:
                count += 1
            if (i, j + 1) in self.grid:
                count += 1
            if (i + 1, j + 1) in self.grid:
                count += 1
            if (i - 1, j + 1) in self.grid:
                count += 1
            if (i + 1, j - 1) in self.grid:
                count += 1
            if (i - 1, j - 1) in self.grid:
                count += 1
            if count == 0:
                if (i + 1, j) not in self.clicked:
                    self.button_clicked(i + 1, j)
                if (i - 1, j) not in self.clicked:
                    self.button_clicked(i - 1, j)
                if (i, j - 1) not in self.clicked:
                    self.button_clicked(i, j - 1)
                if (i, j + 1) not in self.clicked:
                    self.button_clicked(i, j + 1)
                if (i + 1, j + 1) not in self.clicked:
                    self.button_clicked(i + 1, j + 1)
                if (i - 1, j + 1) not in self.clicked:
                    self.button_clicked(i - 1, j + 1)
                if (i + 1, j - 1) not in self.clicked:
                    self.button_clicked(i + 1, j - 1)
                if (i - 1, j - 1) not in self.clicked:
                    self.button_clicked(i - 1, j - 1)
            pressedButton.setEnabled(False)
            pressedButton.setText(str(count))

    def fail(self):
        pass
            