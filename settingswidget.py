from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class SettingsMenu(QWidget):
    def __init__(self, controller, *args, **kwargs):
        super().__init__()
        self.controller = controller

        layout = QVBoxLayout()
        
        settingsLabel = QLabel("Settings")

        layout.addWidget(settingsLabel)

        self.setWindowTitle("Settings")
        self.setLayout(layout)
    
