import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtCore import Qt, QSize

from pages.home_page import HomePage
from pages.stages_page import StagesPage
from pages.classes_page import ClassesPage
from pages.subjects_page import SubjectsPage
from pages.units_page import UnitsPage
from pages.lessons_page import LessonsPage
from pages.updates_page import UpdatesPage


# Global thin modern scrollbar style
SCROLLBAR_STYLE = """
    QScrollBar:vertical {
        background: transparent;
        width: 6px;
        margin: 0;
        border-radius: 3px;
    }
    QScrollBar::handle:vertical {
        background: rgba(142, 45, 226, 0.3);
        min-height: 30px;
        border-radius: 3px;
    }
    QScrollBar::handle:vertical:hover {
        background: rgba(142, 45, 226, 0.55);
    }
    QScrollBar::handle:vertical:pressed {
        background: rgba(142, 45, 226, 0.7);
    }
    QScrollBar::add-line:vertical,
    QScrollBar::sub-line:vertical,
    QScrollBar::add-page:vertical,
    QScrollBar::sub-page:vertical {
        background: none;
        height: 0;
        border: none;
    }
    QScrollBar:horizontal {
        background: transparent;
        height: 6px;
        margin: 0;
        border-radius: 3px;
    }
    QScrollBar::handle:horizontal {
        background: rgba(142, 45, 226, 0.3);
        min-width: 30px;
        border-radius: 3px;
    }
    QScrollBar::handle:horizontal:hover {
        background: rgba(142, 45, 226, 0.55);
    }
    QScrollBar::add-line:horizontal,
    QScrollBar::sub-line:horizontal,
    QScrollBar::add-page:horizontal,
    QScrollBar::sub-page:horizontal {
        background: none;
        width: 0;
        border: none;
    }
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("التطبيق التعليمي")
        self.resize(1300, 750)
        self.setMinimumSize(1000, 600)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ===================== CONTENT AREA =====================
        content_widget = QWidget()
        content_widget.setObjectName("contentArea")
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # ---------- Top Bar ----------
        top_bar = QWidget()
        top_bar.setObjectName("topBar")
        top_bar.setFixedHeight(65)
        top_bar_layout = QHBoxLayout(top_bar)
        top_bar_layout.setContentsMargins(25, 0, 25, 0)

        self.page_title_label = QLabel("الصفحة الرئيسية")
        self.page_title_label.setObjectName("pageTitle")

        search_box = QLineEdit()
        search_box.setPlaceholderText("  🔍  بحث ...")
        search_box.setObjectName("searchBox")
        search_box.setFixedWidth(260)
        search_box.setFixedHeight(38)

        top_bar_layout.addWidget(search_box)
        top_bar_layout.addStretch()
        top_bar_layout.addWidget(self.page_title_label)

        # ---------- Stack ----------
        self.stack = QStackedWidget()
        self.pages = [
            HomePage(self),
            StagesPage(self),
            ClassesPage(self),
            SubjectsPage(self),
            UnitsPage(self),
            LessonsPage(self),
            UpdatesPage(self),
        ]
        for page in self.pages:
            self.stack.addWidget(page)

        content_layout.addWidget(top_bar)
        content_layout.addWidget(self.stack)

        # ===================== SIDEBAR =====================
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(250)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(2)

        # Logo
        logo_frame = QWidget()
        logo_frame.setObjectName("logoFrame")
        logo_frame.setFixedHeight(85)
        logo_inner = QVBoxLayout(logo_frame)
        logo_inner.setAlignment(Qt.AlignCenter)
        logo_text = QLabel("📚  التطبيق التعليمي")
        logo_text.setObjectName("logoText")
        logo_text.setAlignment(Qt.AlignCenter)
        logo_inner.addWidget(logo_text)
        sidebar_layout.addWidget(logo_frame)

        sep = QFrame()
        sep.setFixedHeight(1)
        sep.setStyleSheet("background:rgba(255,255,255,0.12); margin:0 18px;")
        sidebar_layout.addWidget(sep)
        sidebar_layout.addSpacing(15)

        section_lbl = QLabel("  القائمة الرئيسية")
        section_lbl.setObjectName("sectionLabel")
        sidebar_layout.addWidget(section_lbl)
        sidebar_layout.addSpacing(6)

        buttons_data = [
            ("الصفحة الرئيسية", "🏠"),
            ("المرحلة الدراسية", "🎓"),
            ("الفصول", "🏫"),
            ("المواد", "📘"),
            ("الوحدات", "📋"),
            ("الدروس", "📝"),
            ("التحديث", "🔄"),
        ]

        self.menu_buttons = []
        for idx, (text, emoji) in enumerate(buttons_data):
            btn = QPushButton(f"  {emoji}   {text}")
            btn.setObjectName("menuBtn")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedHeight(48)
            btn.clicked.connect(lambda checked, i=idx: self.switch_page(i))
            sidebar_layout.addWidget(btn)
            self.menu_buttons.append(btn)

        sidebar_layout.addStretch()

        bottom_lbl = QLabel("الإصدار 1.0.0")
        bottom_lbl.setObjectName("versionLabel")
        bottom_lbl.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(bottom_lbl)
        sidebar_layout.addSpacing(10)

        main_layout.addWidget(content_widget, 1)
        main_layout.addWidget(sidebar, 0)

        self.setStyleSheet(self._build_stylesheet())
        self.switch_page(0)

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)
        titles = [
            "الصفحة الرئيسية", "المرحلة الدراسية", "الفصول",
            "المواد", "الوحدات", "الدروس", "التحديث",
        ]
        self.page_title_label.setText(titles[index])
        for i, btn in enumerate(self.menu_buttons):
            btn.setProperty("active", i == index)
            btn.style().unpolish(btn)
            btn.style().polish(btn)

    @staticmethod
    def _build_stylesheet():
        return SCROLLBAR_STYLE + """
        QWidget { font-family: 'Segoe UI', 'Cairo', 'Tahoma', sans-serif; }

        #sidebar {
            background: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #4A00E0, stop:1 #8E2DE2
            );
        }
        #logoFrame { background: transparent; }
        #logoText {
            color: #fff; font-size: 20px; font-weight: bold; background: transparent;
        }
        #sectionLabel {
            color: rgba(255,255,255,0.40); font-size: 11px;
            padding-right: 22px; background: transparent;
        }
        #versionLabel {
            color: rgba(255,255,255,0.25); font-size: 11px;
            background: transparent; padding: 8px;
        }
        #menuBtn {
            background: transparent;
            color: rgba(255,255,255,0.68);
            border: none;
            border-left: 3px solid transparent;
            font-size: 14px;
            text-align: right;
            padding-right: 20px;
        }
        #menuBtn:hover {
            background: rgba(255,255,255,0.08);
            color: #fff;
        }
        #menuBtn[active="true"] {
            background: rgba(255,255,255,0.15);
            color: #fff;
            font-weight: bold;
            border-left: 3px solid #fff;
        }
        #topBar {
            background-color: #ffffff;
            border-bottom: 1px solid #eaeaea;
        }
        #pageTitle {
            font-size: 19px; font-weight: bold;
            color: #1a1a2e; background: transparent;
        }
        #searchBox {
            border: 2px solid #ececec;
            border-radius: 19px;
            padding: 0 16px;
            font-size: 13px;
            background: #f7f8fa;
            color: #333;
        }
        #searchBox:focus {
            border-color: #8E2DE2;
            background: #fff;
        }
        #contentArea { background-color: #f0f2f5; }
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 11))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())