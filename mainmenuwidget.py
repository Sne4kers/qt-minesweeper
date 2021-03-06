from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy

class MainMenu(QWidget):
    def __init__(self, window, *args, **kwargs):
        super().__init__()
        self.window = window
        layout = QVBoxLayout()
        
        startButton = QPushButton("Start")
        startButton.clicked.connect(self.window.showGameScreen)

        settingsButton = QPushButton("Settings")
        settingsButton.clicked.connect(self.window.showSettingsMenu)

        quitButton = QPushButton("Quit")
        quitButton.clicked.connect(QApplication.quit)

        spacer = QSpacerItem(20, 40, hPolicy=QSizePolicy.Policy.Expanding, vPolicy=QSizePolicy.Policy.Expanding)
        
        layout.addItem(spacer)
        layout.addWidget(startButton)
        layout.addWidget(settingsButton)
        layout.addWidget(quitButton)
        layout.addItem(spacer)

        self.setLayout(layout)