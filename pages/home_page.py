from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

SCROLLBAR_STYLE = """
    QScrollBar:vertical {
        background: transparent; width: 6px; border-radius: 3px;
    }
    QScrollBar::handle:vertical {
        background: rgba(142,45,226,0.3); min-height: 30px; border-radius: 3px;
    }
    QScrollBar::handle:vertical:hover { background: rgba(142,45,226,0.55); }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none; height: 0; border: none;
    }
"""


class StatCard(QFrame):
    def __init__(self, title, value, emoji, accent, parent=None):
        super().__init__(parent)
        self.setObjectName("statCard")
        self.setMinimumHeight(125)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(22)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 30))
        self.setGraphicsEffect(shadow)

        self.setStyleSheet(f"""
            #statCard {{
                background: #fff;
                border-radius: 16px;
                border-top: 3px solid {accent};
            }}
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)

        # Text
        text_box = QVBoxLayout()
        text_box.setSpacing(4)

        lbl_t = QLabel(title)
        lbl_t.setStyleSheet("color:#8e8e93; font-size:12px; background:transparent;")
        lbl_t.setAlignment(Qt.AlignRight)

        lbl_v = QLabel(str(value))
        lbl_v.setStyleSheet("color:#1a1a2e; font-size:28px; font-weight:bold; background:transparent;")
        lbl_v.setAlignment(Qt.AlignRight)

        lbl_c = QLabel("▲ 12% هذا الشهر")
        lbl_c.setStyleSheet("color:#2ecc71; font-size:10px; background:transparent;")
        lbl_c.setAlignment(Qt.AlignRight)

        text_box.addWidget(lbl_t)
        text_box.addWidget(lbl_v)
        text_box.addWidget(lbl_c)
        text_box.addStretch()

        # Icon
        icon_lbl = QLabel(emoji)
        icon_lbl.setFixedSize(50, 50)
        icon_lbl.setAlignment(Qt.AlignCenter)
        icon_lbl.setStyleSheet(f"""
            background: {accent}15;
            color: {accent};
            font-size: 24px;
            border-radius: 25px;
        """)

        layout.addWidget(icon_lbl)
        layout.addStretch()
        layout.addLayout(text_box)


class ActivityRow(QFrame):
    def __init__(self, text, time_text, dot_color="#4361ee", parent=None):
        super().__init__(parent)
        self.setStyleSheet("QFrame{background:transparent; border-bottom:1px solid #f0f0f0;}")
        self.setFixedHeight(48)

        h = QHBoxLayout(self)
        h.setContentsMargins(12, 0, 12, 0)

        dot = QLabel("●")
        dot.setFixedWidth(16)
        dot.setStyleSheet(f"color:{dot_color}; font-size:9px; background:transparent;")
        dot.setAlignment(Qt.AlignCenter)

        label = QLabel(text)
        label.setStyleSheet("color:#333; font-size:13px; background:transparent;")
        label.setAlignment(Qt.AlignRight)

        time_lbl = QLabel(time_text)
        time_lbl.setStyleSheet("color:#aaa; font-size:11px; background:transparent;")
        time_lbl.setAlignment(Qt.AlignLeft)

        h.addWidget(time_lbl)
        h.addStretch()
        h.addWidget(label)
        h.addWidget(dot)


class HomePage(QWidget):
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
        lay.setSpacing(22)

        # ====== Banner ======
        banner = QFrame()
        banner.setObjectName("banner")
        banner.setMinimumHeight(100)
        banner.setStyleSheet("""
            #banner {
                background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
                    stop:0 #4A00E0, stop:1 #8E2DE2);
                border-radius: 16px;
            }
        """)
        sh = QGraphicsDropShadowEffect()
        sh.setBlurRadius(28)
        sh.setOffset(0, 5)
        sh.setColor(QColor(74, 0, 224, 70))
        banner.setGraphicsEffect(sh)

        b_lay = QVBoxLayout(banner)
        b_lay.setContentsMargins(28, 18, 28, 18)
        b_lay.setAlignment(Qt.AlignRight)

        w1 = QLabel("👋  مرحباً بك في لوحة التحكم")
        w1.setStyleSheet("color:#fff; font-size:22px; font-weight:bold; background:transparent;")
        w1.setAlignment(Qt.AlignRight)

        w2 = QLabel("إليك نظرة سريعة على إحصائيات التطبيق اليوم")
        w2.setStyleSheet("color:rgba(255,255,255,0.78); font-size:13px; background:transparent;")
        w2.setAlignment(Qt.AlignRight)

        b_lay.addWidget(w1)
        b_lay.addWidget(w2)
        lay.addWidget(banner)

        # ====== Stats Cards ======
        cards_h = QHBoxLayout()
        cards_h.setSpacing(18)
        for t, v, e, c in [
            ("عدد الزوار", "1,245", "👥", "#4361ee"),
            ("عدد الملفات", "320", "📁", "#2ec4b6"),
            ("عدد الصفحات", "58", "📄", "#e74c3c"),
            ("التحميلات", "5,678", "⬇", "#f4a261"),
        ]:
            cards_h.addWidget(StatCard(t, v, e, c))
        lay.addLayout(cards_h)

        # ====== Bottom Row ======
        bottom = QHBoxLayout()
        bottom.setSpacing(18)

        # -- Activity Panel --
        act_frame = QFrame()
        act_frame.setStyleSheet("background:#fff; border-radius:16px;")
        sh2 = QGraphicsDropShadowEffect()
        sh2.setBlurRadius(20)
        sh2.setOffset(0, 4)
        sh2.setColor(QColor(0, 0, 0, 22))
        act_frame.setGraphicsEffect(sh2)

        a_lay = QVBoxLayout(act_frame)
        a_lay.setContentsMargins(18, 18, 18, 12)
        a_lay.setSpacing(0)

        at = QLabel("📊  آخر النشاطات")
        at.setStyleSheet("font-size:16px; font-weight:bold; color:#1a1a2e; background:transparent; padding-bottom:8px;")
        at.setAlignment(Qt.AlignRight)
        a_lay.addWidget(at)

        for txt, tm, dc in [
            ("تم إضافة درس جديد – الرياضيات", "منذ 5 دقائق", "#4361ee"),
            ("تم تحديث ملف – العلوم الفصل الأول", "منذ 20 دقيقة", "#2ec4b6"),
            ("تم إضافة مرحلة جديدة – الثانوية", "منذ ساعة", "#e74c3c"),
            ("تم رفع 5 ملفات جديدة", "منذ ساعتين", "#f4a261"),
            ("تسجيل دخول مستخدم جديد", "منذ 3 ساعات", "#8E2DE2"),
        ]:
            a_lay.addWidget(ActivityRow(txt, tm, dc))
        a_lay.addStretch()

        # -- Quick Info Panel --
        info_frame = QFrame()
        info_frame.setFixedWidth(280)
        info_frame.setStyleSheet("background:#fff; border-radius:16px;")
        sh3 = QGraphicsDropShadowEffect()
        sh3.setBlurRadius(20)
        sh3.setOffset(0, 4)
        sh3.setColor(QColor(0, 0, 0, 22))
        info_frame.setGraphicsEffect(sh3)

        i_lay = QVBoxLayout(info_frame)
        i_lay.setContentsMargins(20, 20, 20, 20)
        i_lay.setSpacing(14)

        it = QLabel("⚡  معلومات سريعة")
        it.setStyleSheet("font-size:16px; font-weight:bold; color:#1a1a2e; background:transparent;")
        it.setAlignment(Qt.AlignRight)
        i_lay.addWidget(it)

        for label_text, count, color in [
            ("المراحل الدراسية", "6", "#4361ee"),
            ("الفصول الدراسية", "24", "#2ec4b6"),
            ("المواد", "45", "#e74c3c"),
            ("الوحدات", "128", "#f4a261"),
            ("الدروس", "512", "#8E2DE2"),
        ]:
            row = QFrame()
            row.setFixedHeight(48)
            row.setStyleSheet(f"""
                QFrame {{
                    background:{color}08; border-radius:10px;
                    border-right:3px solid {color};
                }}
            """)
            rh = QHBoxLayout(row)
            rh.setContentsMargins(12, 0, 12, 0)

            cl = QLabel(count)
            cl.setStyleSheet(f"color:{color}; font-size:17px; font-weight:bold; background:transparent;")
            cl.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            nl = QLabel(label_text)
            nl.setStyleSheet("color:#555; font-size:13px; background:transparent;")
            nl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

            rh.addWidget(cl)
            rh.addStretch()
            rh.addWidget(nl)
            i_lay.addWidget(row)

        i_lay.addStretch()

        # Progress
        pt = QLabel("📈  نسبة الإنجاز")
        pt.setStyleSheet("color:#888; font-size:12px; background:transparent;")
        pt.setAlignment(Qt.AlignRight)
        i_lay.addWidget(pt)

        pb = QProgressBar()
        pb.setValue(72)
        pb.setFixedHeight(10)
        pb.setTextVisible(False)
        pb.setStyleSheet("""
            QProgressBar {
                background:#f0f0f5; border-radius:5px; border:none;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
                    stop:0 #4A00E0, stop:1 #8E2DE2);
                border-radius:5px;
            }
        """)
        i_lay.addWidget(pb)

        pl = QLabel("72%")
        pl.setStyleSheet("color:#4A00E0; font-size:13px; font-weight:bold; background:transparent;")
        pl.setAlignment(Qt.AlignCenter)
        i_lay.addWidget(pl)

        bottom.addWidget(info_frame)
        bottom.addWidget(act_frame, 1)
        lay.addLayout(bottom)

        # ====== Quick Actions ======
        qf = QFrame()
        qf.setStyleSheet("background:#fff; border-radius:16px;")
        sh4 = QGraphicsDropShadowEffect()
        sh4.setBlurRadius(20)
        sh4.setOffset(0, 4)
        sh4.setColor(QColor(0, 0, 0, 22))
        qf.setGraphicsEffect(sh4)

        ql = QVBoxLayout(qf)
        ql.setContentsMargins(22, 18, 22, 18)
        ql.setSpacing(12)

        qt = QLabel("🚀  إجراءات سريعة")
        qt.setStyleSheet("font-size:16px; font-weight:bold; color:#1a1a2e; background:transparent;")
        qt.setAlignment(Qt.AlignRight)
        ql.addWidget(qt)

        br = QHBoxLayout()
        br.setSpacing(12)
        for bt, bc in [
            ("➕  إضافة درس", "#4361ee"),
            ("📤  رفع ملف", "#2ec4b6"),
            ("🔄  تحديث البيانات", "#8E2DE2"),
            ("📊  تصدير تقرير", "#f4a261"),
        ]:
            ab = QPushButton(bt)
            ab.setCursor(Qt.PointingHandCursor)
            ab.setFixedHeight(44)
            ab.setStyleSheet(f"""
                QPushButton {{
                    background:{bc}; color:#fff; border:none;
                    border-radius:11px; font-size:13px; font-weight:bold; padding:0 18px;
                }}
                QPushButton:hover {{ background:{bc}dd; }}
                QPushButton:pressed {{ background:{bc}bb; }}
            """)
            br.addWidget(ab)
        ql.addLayout(br)
        lay.addWidget(qf)
        lay.addSpacing(15)

        scroll.setWidget(container)
        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(scroll)