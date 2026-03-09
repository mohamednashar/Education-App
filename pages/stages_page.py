from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class StagesPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()

        # زر العودة للرئيسية
        home_btn = QPushButton("الرئيسية")
        home_btn.clicked.connect(lambda: parent.stack.setCurrentIndex(0))
        home_btn.setStyleSheet("padding:10px; font-size:14px; margin-bottom:20px;")
        layout.addWidget(home_btn, alignment=Qt.AlignLeft)

        # عنوان الصفحة
        label = QLabel("المرحلة الدراسية")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size:24px; font-weight:bold; margin-top:50px;")
        layout.addWidget(label)

        self.setLayout(layout)