from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        main_layout = QVBoxLayout(self)

        # لوحة الإحصائيات على الشمال
        stats_layout = QHBoxLayout()
        stats_layout.setAlignment(Qt.AlignLeft)

        stats = [
            ("عدد الزوار", "100", "#ffe0b2"),
            ("عدد الصفحات", "10", "#b2dfdb"),
            ("عدد الملفات", "25", "#c5cae9")
        ]

        for name, value, color in stats:
            lbl = QLabel(f"{name}: {value}")
            lbl.setFont(QFont("Arial", 14))
            lbl.setStyleSheet(f"""
                background-color:{color};
                padding:10px;
                border-radius:5px;
                margin-right:10px;
            """)
            stats_layout.addWidget(lbl)

        main_layout.addLayout(stats_layout)

        # مربع صغير للملفات فوق الشمال
        files_group = QGroupBox("الملفات")
        files_group.setFixedSize(500, 200)  # مربع صغير
        files_layout = QHBoxLayout()

        files = [
            ("PDF", "#ffcdd2"),
            ("Word", "#d1c4e9"),
            ("Video", "#c8e6c9")
        ]
        for name, color in files:
            btn = QPushButton(name)
            btn.setFixedSize(120, 120)
            btn.setStyleSheet(f"""
                background-color:{color};
                font-size:16px;
                border-radius:10px;
            """)
            files_layout.addWidget(btn)

        files_group.setLayout(files_layout)
        main_layout.addWidget(files_group, alignment=Qt.AlignLeft)

        self.setLayout(main_layout)