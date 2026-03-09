import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

from pages.home_page import HomePage
from pages.stages_page import StagesPage
from pages.classes_page import ClassesPage
from pages.subjects_page import SubjectsPage
from pages.units_page import UnitsPage
from pages.lessons_page import LessonsPage
from pages.updates_page import UpdatesPage

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("التطبيق التعليمي")
        self.resize(1300, 750)

        main_layout = QHBoxLayout(self)

        # Stack للصفحات
        self.stack = QStackedWidget()
        self.pages = [
            HomePage(self),
            StagesPage(self),
            ClassesPage(self),
            SubjectsPage(self),
            UnitsPage(self),
            LessonsPage(self),
            UpdatesPage(self)
        ]
        for p in self.pages:
            self.stack.addWidget(p)

        # Sidebar Menu على اليمين
        menu_layout = QVBoxLayout()
        buttons = [
            ("الصفحة الرئيسية", "resources/icons/home.png"),
            ("المرحلة الدراسية", "resources/icons/stage.png"),
            ("الفصول", "resources/icons/classes.png"),
            ("المواد", "resources/icons/subject.png"),
            ("الوحدات", "resources/icons/unit.png"),
            ("الدروس", "resources/icons/lesson.png"),
            ("التحديث", "resources/icons/update.png")
        ]

        self.menu_buttons = {}
        for i, (text, icon_path) in enumerate(buttons):
            btn = QPushButton(text)
            btn.setIcon(QIcon(icon_path))
            btn.setStyleSheet("""
                QPushButton {
                    padding: 12px;
                    text-align: left;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #d0e6ff;
                }
            """)
            btn.clicked.connect(lambda checked, index=i: self.stack.setCurrentIndex(index))
            menu_layout.addWidget(btn)

        menu_layout.addStretch()  # يخلي المنيو واصل لاخر الصفحة
        menu_widget = QWidget()
        menu_widget.setLayout(menu_layout)
        menu_widget.setFixedWidth(220)
        menu_widget.setStyleSheet("background-color: #f0f0f0;")

        main_layout.addWidget(self.stack)
        main_layout.addWidget(menu_widget)
        self.setLayout(main_layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())