from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class UnitsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()

        home_btn = QPushButton("الرئيسية")
        home_btn.clicked.connect(lambda: parent.stack.setCurrentIndex(0))
        layout.addWidget(home_btn)

        label = QLabel("الوحدات")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.setLayout(layout)