# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_view.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QCommandLinkButton,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Attendace_History(object):
    def setupUi(self, Attendace_History):
        if not Attendace_History.objectName():
            Attendace_History.setObjectName(u"Attendace_History")
        Attendace_History.resize(1366, 768)
        self.back_button = QPushButton(Attendace_History)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(20, 20, 91, 41))
        self.tittle = QLineEdit(Attendace_History)
        self.tittle.setObjectName(u"tittle")
        self.tittle.setGeometry(QRect(250, 30, 871, 61))
        font = QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.tittle.setFont(font)
        self.tittle.setAlignment(Qt.AlignCenter)
        self.viewer_widget = QWidget(Attendace_History)
        self.viewer_widget.setObjectName(u"viewer_widget")
        self.viewer_widget.setGeometry(QRect(80, 110, 1051, 631))
        self.calendar = QCalendarWidget(self.viewer_widget)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setGeometry(QRect(700, 180, 312, 190))
        self.view_calendar = QCommandLinkButton(self.viewer_widget)
        self.view_calendar.setObjectName(u"view_calendar")
        self.view_calendar.setGeometry(QRect(660, 180, 41, 31))
        icon = QIcon()
        icon.addFile(u"C:/Users/Admin/Downloads/calendar-icon-isolated-white-background-calender-symbol-vector-deadline-date-time-185768346.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.view_calendar.setIcon(icon)
        self.view_calendar.setIconSize(QSize(15, 22))
        self.date_picker = QComboBox(self.viewer_widget)
        self.date_picker.addItem("")
        self.date_picker.setObjectName(u"date_picker")
        self.date_picker.setGeometry(QRect(210, 180, 491, 31))
        self.date_picker.raise_()
        self.view_calendar.raise_()
        self.calendar.raise_()

        self.retranslateUi(Attendace_History)

        QMetaObject.connectSlotsByName(Attendace_History)
    # setupUi

    def retranslateUi(self, Attendace_History):
        Attendace_History.setWindowTitle(QCoreApplication.translate("Attendace_History", u"Form", None))
        self.back_button.setText(QCoreApplication.translate("Attendace_History", u"Back", None))
        self.tittle.setText(QCoreApplication.translate("Attendace_History", u"L\u1ecbch s\u1eed \u0111i\u1ec3m danh", None))
        self.view_calendar.setText("")
        self.date_picker.setItemText(0, QCoreApplication.translate("Attendace_History", u"test", None))

    # retranslateUi

