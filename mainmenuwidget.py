from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class MainMenu(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        startButton = QPushButton("Start")
        settingsButton = QPushButton("Settings")
        quitButton = QPushButton("Quit")

        layout.addWidget(startButton)
        layout.addWidget(settingsButton)
        layout.addWidget(quitButton)

        self.setLayout(layout)
