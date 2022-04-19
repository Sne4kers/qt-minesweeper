from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from gameareabutton import MineButton

import random

class GameArea(QWidget):
    gameEnded = pyqtSignal(name="gameEnded")
    markedCell = pyqtSignal(int)
    gameWon = pyqtSignal()

    def __init__(self, gridSize, numberMines, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid = {}
        self.width = gridSize[0]
        self.height = gridSize[1]
        self.clicked = {}
        self.marked = {}
        self.adjacency_list = [
            (1, 0),
            (1, -1),
            (1, 1),
            (-1, 0),
            (-1, 1),
            (-1, -1),
            (0, 1),
            (0, -1)
            ]
        self.gridButtonLayout = QGridLayout()
        self.gridButtonLayout.setSpacing(0)
        for i in range(self.height):
            for j in range(self.width):
                button = MineButton()
                button.setMinimumSize(QSize(20, 20))
                button.setMaximumSize(QSize(30, 30))
                button.setStyleSheet('QPushButton {background-color: #808080}')
                button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
                button.clicked.connect(lambda j=j, i=i: self.button_clicked(i, j, True))
                button.marked.connect(lambda j=j, i=i: self.button_marked(i, j))
                self.gridButtonLayout.addWidget(button, i, j)
        self.setLayout(self.gridButtonLayout)
        for i in range(numberMines):
            xRandomMine = random.randint(0, self.width - 1)
            yRandomMine = random.randint(0, self.height - 1)
            while (yRandomMine, xRandomMine) in self.grid:
                xRandomMine = random.randint(0, self.width - 1)
                yRandomMine = random.randint(0, self.height - 1)
            self.grid[(yRandomMine, xRandomMine)] = -1

    def button_clicked(self, i, j, manual):
        if (i, j) in self.marked:
            return
        if (i, j) in self.clicked:
            return
        if i < 0 or j < 0 or i >= self.height or j >= self.width:
            return
        self.clicked[(i, j)] = True
        pressedButton = self.gridButtonLayout.itemAtPosition(i, j).widget()
        if (i, j) in self.grid:
            if len(self.clicked) == 1:
                while (i, j) in self.grid:
                    self.generate_new_schema()
                self.button_clicked(i, j, True)
            else:
                self.fail()
                pressedButton.setText("B")
                pressedButton.setStyleSheet('QPushButton {background-color: #FF0000}')
        else:
            if self.check_win():
                self.gameWon.emit()
            count = self.get_value(i, j)
            if count == 0:
                for pair in self.adjacency_list:
                    if (i + pair[0], j + pair[1]):
                        self.button_clicked(i + pair[0], j + pair[1], False)
            elif manual:
                for pair in self.adjacency_list:
                    if (i + pair[0], j + pair[1]) and self.get_value(i + pair[0], j + pair[1]) == 0 and not (i + pair[0], j + pair[1]) in self.grid:
                        self.button_clicked(i + pair[0], j + pair[1], False)
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
        self.gameEnded.emit()
        for bombCord in self.grid:
            pressedButton = self.gridButtonLayout.itemAtPosition(bombCord[0], bombCord[1]).widget()
            pressedButton.setStyleSheet('QPushButton {background-color: #FF8888}')
        for i in range(self.height):
            for j in range(self.width):
                button = self.gridButtonLayout.itemAtPosition(i, j).widget()
                button.setEnabled(False)

    def button_marked(self, i, j):
        pressedButton = self.gridButtonLayout.itemAtPosition(i, j).widget()
        if (i, j) in self.marked:
            self.markedCell.emit(1)
            self.marked.pop((i, j))
            pressedButton.setText("")
        else:
            self.markedCell.emit(-1)
            self.marked[(i, j)] = True
            pressedButton.setText("M")

        if self.check_win():
            self.gameWon.emit()

    def generate_new_schema(self):
        numberMines = len(self.grid)
        self.clicked = {}
        self.marked = {}
        self.grid = {}
        for i in range(self.height):
            for j in range(self.width):
                button = self.gridButtonLayout.itemAtPosition(i, j).widget()
                button.clicked.disconnect()
                button.marked.disconnect()
                button.clicked.connect(lambda j=j, i=i: self.button_clicked(i, j, True))
                button.marked.connect(lambda j=j, i=i: self.button_marked(i, j))
        for i in range(numberMines):
            xRandomMine = random.randint(0, self.width - 1)
            yRandomMine = random.randint(0, self.height - 1)
            while (yRandomMine, xRandomMine) in self.grid:
                xRandomMine = random.randint(0, self.width - 1)
                yRandomMine = random.randint(0, self.height - 1)
            self.grid[(yRandomMine, xRandomMine)] = -1

    def check_win(self):
        if len(self.marked) + len(self.clicked) == self.width * self.height and len(self.marked) == len(self.grid):
            return True
        else:
            return False

    def get_value(self, i, j):
        count = 0
        for pair in self.adjacency_list:
            if (i + pair[0], j + pair[1]) in self.grid:
                count += 1
        return count