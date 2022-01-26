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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

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
        self.calendar.setGeometry(QRect(640, 110, 312, 190))
        self.view_calendar = QCommandLinkButton(self.viewer_widget)
        self.view_calendar.setObjectName(u"view_calendar")
        self.view_calendar.setGeometry(QRect(600, 110, 41, 31))
        icon = QIcon()
        icon.addFile(u"C:/Users/Admin/Downloads/calendar-icon-isolated-white-background-calender-symbol-vector-deadline-date-time-185768346.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.view_calendar.setIcon(icon)
        self.view_calendar.setIconSize(QSize(15, 22))
        self.date_picker = QComboBox(self.viewer_widget)
        self.date_picker.setObjectName(u"date_picker")
        self.date_picker.setGeometry(QRect(150, 110, 491, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.date_picker.setFont(font1)
        self.date_picker_label = QLabel(self.viewer_widget)
        self.date_picker_label.setObjectName(u"date_picker_label")
        self.date_picker_label.setGeometry(QRect(30, 110, 121, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.date_picker_label.setFont(font2)
        self.search_button = QPushButton(self.viewer_widget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(900, 90, 128, 64))
        self.tableWidget = QTableWidget(self.viewer_widget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 290, 1011, 301))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.pushButton = QPushButton(self.viewer_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(900, 170, 128, 64))
        self.date_picker.raise_()
        self.view_calendar.raise_()
        self.calendar.raise_()
        self.date_picker_label.raise_()
        self.search_button.raise_()
        self.tableWidget.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Attendace_History)

        QMetaObject.connectSlotsByName(Attendace_History)
    # setupUi

    def retranslateUi(self, Attendace_History):
        Attendace_History.setWindowTitle(QCoreApplication.translate("Attendace_History", u"Form", None))
        self.back_button.setText(QCoreApplication.translate("Attendace_History", u"Back", None))
        self.tittle.setText(QCoreApplication.translate("Attendace_History", u"L\u1ecbch s\u1eed \u0111i\u1ec3m danh", None))
        self.view_calendar.setText("")
        self.date_picker_label.setText(QCoreApplication.translate("Attendace_History", u"Th\u1eddi gian:", None))
        self.search_button.setText(QCoreApplication.translate("Attendace_History", u"T\u00ecm ki\u1ebfm", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Attendace_History", u"MSSV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Attendace_History", u"T\u00ean sinh vi\u00ean", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Attendace_History", u"Email", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Attendace_History", u"Th\u1eddi gian \u0111i\u1ec3m danh", None));
        self.pushButton.setText(QCoreApplication.translate("Attendace_History", u"Xu\u1ea5t b\u00e1o c\u00e1o", None))
    # retranslateUi

