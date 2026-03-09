from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()

        # Dashboard إحصائيات
        stats_layout = QHBoxLayout()
        for text in ["عدد الزوار: 100", "عدد الصفحات: 10", "عدد الملفات: 25"]:
            lbl = QLabel(text)
            lbl.setFont(QFont("Arial", 14))
            lbl.setStyleSheet("background-color:#e0f7fa; padding:10px; border-radius:5px;")
            stats_layout.addWidget(lbl)
        layout.addLayout(stats_layout)

        # مساحة الملفات
        files_layout = QHBoxLayout()
        files = [
            ("PDF", "#ffcdd2"),
            ("Word", "#d1c4e9"),
            ("Video", "#c8e6c9")
        ]
        for name, color in files:
            btn = QPushButton(name)
            btn.setFixedSize(150, 150)
            btn.setStyleSheet(f"background-color:{color}; font-size:16px; border-radius:10px;")
            files_layout.addWidget(btn)
        layout.addLayout(files_layout)

        self.setLayout(layout)