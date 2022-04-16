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
                button.setStyleSheet('QPushButton {background-color: #808080}')
                button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
                button.clicked.connect(lambda ch, j=j, i=i: self.button_clicked(i, j))
                self.gridButtonLayout.addWidget(button, i, j)
        self.setLayout(self.gridButtonLayout)
        for i in range(numberMines):
            xRandomMine = random.randint(0, self.width - 1)
            yRandomMine = random.randint(0, self.height - 1)
            while (yRandomMine, xRandomMine) in self.grid:
                xRandomMine = random.randint(0, self.width - 1)
                yRandomMine = random.randint(0, self.height - 1)
            self.grid[(yRandomMine, xRandomMine)] = -1

    def button_clicked(self, i, j):
        self.clicked[(i, j)] = True
        if i < 0 or j < 0 or i >= self.height or j >= self.width:
            return
        pressedButton = self.gridButtonLayout.itemAtPosition(i, j).widget()
        if (i, j) in self.grid:
            self.fail()
            pressedButton.setText("B")
            pressedButton.setStyleSheet('QPushButton {background-color: #FF0000}')
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
            if count != 0:
                pressedButton.setText(str(count))
            pressedButton.setStyleSheet(self.getTextStyleSheet(count))

    def getTextStyleSheet(self, count):
        if count == 0:
            return 'QPushButton {background-color: #000000; color: #000000; border: none}'
        elif count == 1:
            return 'QPushButton {background-color: #000000; color: #EE3030; border: none}'
        elif count == 2:
            return 'QPushButton {background-color: #000000; color: #30EE30; border: none}'
        elif count == 3:
            return 'QPushButton {background-color: #000000; color: #3030EE; border: none}'
        elif count >= 4:
            return 'QPushButton {background-color: #000000; color: #AA00AA; border: none}'

    def fail(self):
        for bombCord in self.grid:
            print(bombCord[1])
            print(bombCord[0])
            pressedButton = self.gridButtonLayout.itemAtPosition(bombCord[0], bombCord[1]).widget()
            pressedButton.setStyleSheet('QPushButton {background-color: #FF8888}')
        for i in range(self.height):
            for j in range(self.width):
                button = self.gridButtonLayout.itemAtPosition(i, j).widget()
                button.setEnabled(False)
