from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

SCROLLBAR_STYLE = """
    QScrollBar:vertical {
        background:transparent; width:6px; border-radius:3px;
    }
    QScrollBar::handle:vertical {
        background:rgba(142,45,226,0.3); min-height:30px; border-radius:3px;
    }
    QScrollBar::handle:vertical:hover { background:rgba(142,45,226,0.55); }
    QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical,
    QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {
        background:none; height:0; border:none;
    }
"""


def make_shadow(parent=None, blur=22, dy=4, alpha=28):
    s = QGraphicsDropShadowEffect(parent)
    s.setBlurRadius(blur)
    s.setOffset(0, dy)
    s.setColor(QColor(0, 0, 0, alpha))
    return s


def make_action_btn(emoji, bg, hover_bg):
    b = QPushButton(emoji)
    b.setFixedSize(32, 32)
    b.setCursor(Qt.PointingHandCursor)
    b.setStyleSheet(f"""
        QPushButton {{ background:{bg}; border:none; border-radius:8px; font-size:15px; }}
        QPushButton:hover {{ background:{hover_bg}; }}
    """)
    return b


def build_table(headers, data, parent=None):
    table = QTableWidget(parent)
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)
    table.horizontalHeader().setStretchLastSection(True)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.setAlternatingRowColors(True)
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    table.verticalHeader().setVisible(False)
    table.setShowGrid(False)
    table.setStyleSheet("""
        QTableWidget {
            background:#fff; border:none; border-radius:14px;
            gridline-color:#f5f5f5; font-size:13px;
        }
        QTableWidget::item {
            padding:10px; border-bottom:1px solid #f2f2f2;
        }
        QTableWidget::item:selected {
            background:#EDE7F6; color:#333;
        }
        QHeaderView::section {
            background:#fafafa; color:#777; font-weight:bold;
            font-size:12px; border:none; padding:12px 8px;
            border-bottom:2px solid #e8e8e8;
        }
    """ + SCROLLBAR_STYLE)
    table.setGraphicsEffect(make_shadow(parent))

    table.setRowCount(len(data))
    for row, row_data in enumerate(data):
        for col, val in enumerate(row_data):
            table.setItem(row, col + 1, QTableWidgetItem(val))
        table.setRowHeight(row, 52)

        # Action cell
        aw = QWidget()
        al = QHBoxLayout(aw)
        al.setContentsMargins(6, 4, 6, 4)
        al.setSpacing(5)
        al.addWidget(make_action_btn("🗑️", "#FFEBEE", "#FFCDD2"))
        al.addWidget(make_action_btn("✏️", "#EDE7F6", "#D1C4E9"))
        al.addStretch()
        table.setCellWidget(row, 0, aw)

    return table


def build_top_bar(add_text, search_placeholder):
    bar = QHBoxLayout()

    add_btn = QPushButton(add_text)
    add_btn.setCursor(Qt.PointingHandCursor)
    add_btn.setFixedHeight(40)
    add_btn.setStyleSheet("""
        QPushButton {
            background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
                stop:0 #4A00E0, stop:1 #8E2DE2);
            color:#fff; border:none; border-radius:11px;
            font-size:13px; font-weight:bold; padding:0 22px;
        }
        QPushButton:hover { background:#6B21A8; }
    """)

    search = QLineEdit()
    search.setPlaceholderText(search_placeholder)
    search.setFixedWidth(240)
    search.setFixedHeight(40)
    search.setStyleSheet("""
        QLineEdit {
            border:2px solid #e0e0e0; border-radius:11px;
            padding:0 14px; font-size:13px; background:#fff;
        }
        QLineEdit:focus { border-color:#8E2DE2; }
    """)

    bar.addWidget(add_btn)
    bar.addStretch()
    bar.addWidget(search)
    return bar


class StagesPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background:#f0f2f5;")

        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setStyleSheet("background:transparent; border:none;" + SCROLLBAR_STYLE)

        container = QWidget()
        lay = QVBoxLayout(container)
        lay.setContentsMargins(30, 25, 30, 25)
        lay.setSpacing(18)

        header = QLabel("🎓  إدارة المراحل الدراسية")
        header.setStyleSheet("font-size:20px; font-weight:bold; color:#1a1a2e; background:transparent;")
        header.setAlignment(Qt.AlignRight)
        lay.addWidget(header)

        lay.addLayout(build_top_bar("➕  إضافة مرحلة جديدة", "🔍  بحث في المراحل ..."))

        data = [
            ("المرحلة الابتدائية", "التعليم الأساسي - المرحلة الأولى", "6"),
            ("المرحلة المتوسطة", "التعليم الأساسي - المرحلة الثانية", "3"),
            ("المرحلة الثانوية", "التعليم الثانوي العام", "3"),
            ("رياض الأطفال", "مرحلة ما قبل التعليم الأساسي", "2"),
        ]
        table = build_table(["الإجراءات", "عدد الفصول", "الوصف", "اسم المرحلة"], data, self)
        lay.addWidget(table)

        scroll.setWidget(container)
        page_lay = QVBoxLayout(self)
        page_lay.setContentsMargins(0, 0, 0, 0)
        page_lay.addWidget(scroll)