from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from pages.stages_page import build_table, build_top_bar, make_shadow, SCROLLBAR_STYLE


class ClassesPage(QWidget):
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

        header = QLabel("🏫  إدارة الفصول الدراسية")
        header.setStyleSheet("font-size:20px; font-weight:bold; color:#1a1a2e; background:transparent;")
        header.setAlignment(Qt.AlignRight)
        lay.addWidget(header)

        # Stats mini cards
        stats_row = QHBoxLayout()
        stats_row.setSpacing(14)
        for title, val, color in [
            ("إجمالي الفصول", "24", "#4361ee"),
            ("فصول نشطة", "20", "#2ec4b6"),
            ("فصول مغلقة", "4", "#e74c3c"),
        ]:
            card = QFrame()
            card.setFixedHeight(80)
            card.setStyleSheet(f"""
                QFrame {{
                    background:#fff; border-radius:14px;
                    border-top:3px solid {color};
                }}
            """)
            card.setGraphicsEffect(make_shadow(self))
            cl = QVBoxLayout(card)
            cl.setAlignment(Qt.AlignCenter)
            vl = QLabel(val)
            vl.setStyleSheet(f"color:{color}; font-size:24px; font-weight:bold; background:transparent;")
            vl.setAlignment(Qt.AlignCenter)
            tl = QLabel(title)
            tl.setStyleSheet("color:#888; font-size:12px; background:transparent;")
            tl.setAlignment(Qt.AlignCenter)
            cl.addWidget(vl)
            cl.addWidget(tl)
            stats_row.addWidget(card)
        lay.addLayout(stats_row)

        lay.addLayout(build_top_bar("➕  إضافة فصل جديد", "🔍  بحث في الفصول ..."))

        data = [
            ("الصف الأول الابتدائي", "المرحلة الابتدائية", "35", "نشط"),
            ("الصف الثاني الابتدائي", "المرحلة الابتدائية", "32", "نشط"),
            ("الصف الأول المتوسط", "المرحلة المتوسطة", "28", "نشط"),
            ("الصف الأول الثانوي", "المرحلة الثانوية", "30", "نشط"),
            ("الصف الثالث الثانوي", "المرحلة الثانوية", "25", "مغلق"),
        ]
        table = build_table(
            ["الإجراءات", "الحالة", "عدد الطلاب", "المرحلة", "اسم الفصل"], data, self
        )
        lay.addWidget(table)

        scroll.setWidget(container)
        page_lay = QVBoxLayout(self)
        page_lay.setContentsMargins(0, 0, 0, 0)
        page_lay.addWidget(scroll)