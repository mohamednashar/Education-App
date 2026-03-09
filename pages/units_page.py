from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from pages.stages_page import build_table, build_top_bar, make_shadow, SCROLLBAR_STYLE


class UnitsPage(QWidget):
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

        header = QLabel("📋  إدارة الوحدات")
        header.setStyleSheet("font-size:20px; font-weight:bold; color:#1a1a2e; background:transparent;")
        header.setAlignment(Qt.AlignRight)
        lay.addWidget(header)

        stats_row = QHBoxLayout()
        stats_row.setSpacing(14)
        for title, val, color in [
            ("إجمالي الوحدات", "128", "#4361ee"),
            ("وحدات مكتملة", "96", "#2ec4b6"),
            ("وحدات قيد التحديث", "32", "#f4a261"),
        ]:
            card = QFrame()
            card.setFixedHeight(80)
            card.setStyleSheet(f"QFrame{{ background:#fff; border-radius:14px; border-top:3px solid {color}; }}")
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

        lay.addLayout(build_top_bar("➕  إضافة وحدة جديدة", "🔍  بحث في الوحدات ..."))

        data = [
            ("الوحدة الأولى - الأعداد", "الرياضيات", "الصف الأول", "8", "مكتمل"),
            ("الوحدة الثانية - الجمع", "الرياضيات", "الصف الأول", "6", "مكتمل"),
            ("الوحدة الأولى - النبات", "العلوم", "الصف الثاني", "5", "قيد التحديث"),
            ("الوحدة الأولى - القراءة", "اللغة العربية", "الصف الثالث", "7", "مكتمل"),
            ("الوحدة الثالثة - الحيوان", "العلوم", "الصف الرابع", "4", "قيد التحديث"),
        ]
        table = build_table(
            ["الإجراءات", "الحالة", "عدد الدروس", "الفصل", "المادة", "اسم الوحدة"], data, self
        )
        lay.addWidget(table)

        scroll.setWidget(container)
        page_lay = QVBoxLayout(self)
        page_lay.setContentsMargins(0, 0, 0, 0)
        page_lay.addWidget(scroll)