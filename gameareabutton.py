from PyQt6.QtWidgets import QPushButton, QWidget
from PyQt6.QtCore import Qt, pyqtSignal

class MineButton(QPushButton):
    clicked = pyqtSignal()
    marked = pyqtSignal()

    def __init__(self):
        super().__init__()
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            self.marked.emit()
        elif event.button() == Qt.MouseButton.LeftButton:
            print("left")
            self.clicked.emit()
        event.accept()