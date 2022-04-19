from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpinBox, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt

class SettingsMenu(QWidget):
    def __init__(self, window, *args, **kwargs):
        super().__init__()
        self.window = window
        self.width = 8
        self.height = 16
        self.mines = 20
        
        self.minesSpinBox = QSpinBox()
        self.minesSpinBox.setMinimum(int(self.height * self.width * 0.05))
        self.minesSpinBox.setMaximum(int(self.height * self.width * 0.2))
        self.minesSpinBox.setValue(self.mines)
        self.minesSpinBox.valueChanged.connect(self.updateMines)

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
        
        self.widthSpinBox = QSpinBox()
        self.widthSpinBox.setMinimum(5)
        self.widthSpinBox.setMaximum(20)
        self.widthSpinBox.setValue(self.width)
        self.widthSpinBox.valueChanged.connect(self.updateSize)

        widthHBox = QHBoxLayout()
        widthHBox.addWidget(gameAreaWidthLabel)
        widthHBox.addWidget(self.widthSpinBox)
        

        gameAreaHeightLabel = QLabel("Area height")
        gameAreaHeightLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.heightSpinBox = QSpinBox()
        self.heightSpinBox.setMinimum(10)
        self.heightSpinBox.setMaximum(30)
        self.heightSpinBox.setValue(self.height)
        self.heightSpinBox.valueChanged.connect(self.updateSize)

        heightHBox = QHBoxLayout()
        heightHBox.addWidget(gameAreaHeightLabel)
        heightHBox.addWidget(self.heightSpinBox)

        minesLabel = QLabel("Number of mines")
        minesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        minesHBox = QHBoxLayout()
        minesHBox.addWidget(minesLabel)
        minesHBox.addWidget(self.minesSpinBox)

        spacer = QSpacerItem(20, 40, hPolicy=QSizePolicy.Policy.Expanding, vPolicy=QSizePolicy.Policy.Expanding)

        layout = QVBoxLayout()
        layout.addItem(spacer)
        layout.addLayout(settingsHBox)
        layout.addLayout(widthHBox)
        layout.addLayout(heightHBox)
        layout.addLayout(minesHBox)
        layout.addItem(spacer)

        self.setLayout(layout)

    def getAreaSize(self):
        return (self.width, self.height)
    
    def getNumberOfMines(self):
        return self.mines

    def updateSize(self):
        self.height = self.heightSpinBox.value()
        self.width = self.widthSpinBox.value()
        self.minesSpinBox.setMinimum(int(self.height * self.width * 0.05))
        self.minesSpinBox.setMaximum(int(self.height * self.width * 0.2))
    
    def updateMines(self):
        self.mines = self.minesSpinBox.value()
    
