from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainMenu(QWidget):
    def __init__(self, controller, *args, **kwargs):
        super().__init__()
        self.controller = controller
        layout = QVBoxLayout()
        
        startButton = QPushButton("Start")
        settingsButton = QPushButton("Settings")
        settingsButton.clicked.connect(self.controller.showSettingsMenu)

        quitButton = QPushButton("Quit")
        quitButton.clicked.connect(QApplication.quit)

        layout.addWidget(startButton)
        layout.addWidget(settingsButton)
        layout.addWidget(quitButton)

        self.setWindowTitle("Splash")
        self.setLayout(layout)