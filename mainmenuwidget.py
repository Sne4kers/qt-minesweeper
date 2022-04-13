from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainMenu(QWidget):
    def __init__(self, window, *args, **kwargs):
        super().__init__()
        self.window = window
        layout = QVBoxLayout()
        
        startButton = QPushButton("Start")
        
        settingsButton = QPushButton("Settings")
        settingsButton.clicked.connect(self.window.showSettingsMenu)

        quitButton = QPushButton("Quit")
        quitButton.clicked.connect(QApplication.quit)

        layout.addWidget(startButton)
        layout.addWidget(settingsButton)
        layout.addWidget(quitButton)

        self.setLayout(layout)