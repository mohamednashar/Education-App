from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from pages.stages_page import make_shadow, SCROLLBAR_STYLE


class UpdateCard(QFrame):
    def __init__(self, version, date, changes, is_current=False, parent=None):
        super().__init__(parent)
        accent = "#8E2DE2" if is_current else "#e0e0e0"
        badge_bg = "#8E2DE2" if is_current else "#ccc"
        badge_text = "الحالي" if is_current else "سابق"

        self.setStyleSheet(f"""
            QFrame {{
                background:#fff; border-radius:14px;
                border-right:4px solid {accent};
            }}
        """)
        self.setGraphicsEffect(make_shadow(parent))

        lay = QVBoxLayout(self)
        lay.setContentsMargins(22, 18, 22, 18)
        lay.setSpacing(10)

        # Header row
        top = QHBoxLayout()

        badge = QLabel(badge_text)
        badge.setFixedHeight(26)
        badge.setStyleSheet(f"""
            background:{badge_bg}; color:#fff; font-size:11px;
            font-weight:bold; border-radius:13px; padding:0 14px;
        """)

        date_lbl = QLabel(date)
        date_lbl.setStyleSheet("color:#aaa; font-size:12px; background:transparent;")

        ver_lbl = QLabel(f"الإصدار {version}")
        ver_lbl.setStyleSheet("color:#1a1a2e; font-size:17px; font-weight:bold; background:transparent;")

        top.addWidget(badge)
        top.addWidget(date_lbl)
        top.addStretch()
        top.addWidget(ver_lbl)
        lay.addLayout(top)

        # Changes list
        for change in changes:
            cl = QLabel(f"  ●  {change}")
            cl.setStyleSheet("color:#555; font-size:13px; background:transparent; padding:2px 0;")
            cl.setAlignment(Qt.AlignRight)
            lay.addWidget(cl)


class UpdatesPage(QWidget):
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

        header = QLabel("🔄  سجل التحديثات")
        header.setStyleSheet("font-size:20px; font-weight:bold; color:#1a1a2e; background:transparent;")
        header.setAlignment(Qt.AlignRight)
        lay.addWidget(header)

        # Check for updates button
        check_btn = QPushButton("🔍  التحقق من وجود تحديثات")
        check_btn.setCursor(Qt.PointingHandCursor)
        check_btn.setFixedHeight(44)
        check_btn.setFixedWidth(260)
        check_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
                    stop:0 #4A00E0, stop:1 #8E2DE2);
                color:#fff; border:none; border-radius:12px;
                font-size:14px; font-weight:bold;
            }
            QPushButton:hover { background:#6B21A8; }
        """)
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        btn_row.addWidget(check_btn)
        lay.addLayout(btn_row)

        # Update cards
        updates_data = [
            ("1.0.0", "2025-01-15", [
                "إطلاق النسخة الأولى من التطبيق",
                "إضافة نظام إدارة المراحل الدراسية",
                "إضافة نظام إدارة الفصول والمواد",
                "إضافة لوحة التحكم الرئيسية",
                "دعم رفع الملفات المتعددة",
            ], True),
            ("0.9.0", "2024-12-20", [
                "نسخة تجريبية - اختبار الواجهة",
                "إضافة نظام البحث",
                "تحسين أداء قاعدة البيانات",
            ], False),
            ("0.8.0", "2024-11-10", [
                "نسخة ألفا - الهيكل الأساسي",
                "تصميم قاعدة البيانات",
                "إنشاء الصفحات الأساسية",
            ], False),
            ("0.7.0", "2024-10-01", [
                "نموذج أولي للتطبيق",
                "تجربة واجهة المستخدم",
            ], False),
        ]

        for ver, date, changes, is_current in updates_data:
            lay.addWidget(UpdateCard(ver, date, changes, is_current, self))

        lay.addSpacing(20)

        scroll.setWidget(container)
        page_lay = QVBoxLayout(self)
        page_lay.setContentsMargins(0, 0, 0, 0)
        page_lay.addWidget(scroll)