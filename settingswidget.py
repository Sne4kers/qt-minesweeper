from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpinBox, QPushButton
from PyQt6.QtCore import Qt

class SettingsMenu(QWidget):
    def __init__(self, window, *args, **kwargs):
        super().__init__()
        self.window = window
        self.width = 8
        self.height = 16
        
        backButton = QPushButton("<-")
        backButton.setFixedSize(30, 30)
        backButton.clicked.connect(self.window.showMainMenu)

        settingsLabel = QLabel("Settings")
        settingsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        settingsHBox = QHBoxLayout()
        settingsHBox.addWidget(backButton)
        settingsHBox.addWidget(settingsLabel)


        gameAreaWidthLabel = QLabel("Area width")
        gameAreaWidthLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        widthSpinBox = QSpinBox()
        widthSpinBox.setMinimum(5)
        widthSpinBox.setMaximum(20)
        widthSpinBox.setValue(self.width)

        widthHBox = QHBoxLayout()
        widthHBox.addWidget(gameAreaWidthLabel)
        widthHBox.addWidget(widthSpinBox)
        

        gameAreaHeightLabel = QLabel("Area height")
        gameAreaHeightLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        heightSpinBox = QSpinBox()
        heightSpinBox.setMinimum(10)
        heightSpinBox.setMaximum(30)
        heightSpinBox.setValue(self.height)

        heightHBox = QHBoxLayout()
        heightHBox.addWidget(gameAreaHeightLabel)
        heightHBox.addWidget(heightSpinBox)


        layout = QVBoxLayout()
        layout.addLayout(settingsHBox)
        layout.addLayout(widthHBox)
        layout.addLayout(heightHBox)

        self.setLayout(layout)

    def getAreaSize(self):
        return (self.width, self.height)
    
