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
from PySide6.QtWidgets import (QApplication, QLineEdit, QListView, QPushButton,
    QSizePolicy, QWidget, QAbstractItemView)

class Ui_Attendace_History(object):
    def setupUi(self, Attendace_History):
        if not Attendace_History.objectName():
            Attendace_History.setObjectName(u"Attendace_History")
        Attendace_History.resize(1366, 768)
        self.back_button = QPushButton(Attendace_History)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(20, 20, 91, 41))
        self.history_view = QListView(Attendace_History)
        self.history_view.setObjectName(u"history_view")
        self.history_view.setGeometry(QRect(260, 190, 861, 521))
        self.history_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
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

        self.retranslateUi(Attendace_History)

        QMetaObject.connectSlotsByName(Attendace_History)
    # setupUi

    def retranslateUi(self, Attendace_History):
        Attendace_History.setWindowTitle(QCoreApplication.translate("Attendace_History", u"Form", None))
        self.back_button.setText(QCoreApplication.translate("Attendace_History", u"Back", None))
        self.tittle.setText(QCoreApplication.translate("Attendace_History", u"L\u1ecbch s\u1eed \u0111i\u1ec3m danh", None))
    # retranslateUi

