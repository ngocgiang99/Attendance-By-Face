# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'attendance.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Attendance(object):
    def setupUi(self, Attendance):
        if not Attendance.objectName():
            Attendance.setObjectName(u"Attendance")
        Attendance.resize(1366, 768)
        self.back_button = QPushButton(Attendance)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(20, 20, 91, 31))
        self.back_button.setCheckable(True)
        self.info_line = QLineEdit(Attendance)
        self.info_line.setObjectName(u"info_line")
        self.info_line.setGeometry(QRect(160, 21, 1171, 61))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        self.info_line.setFont(font)
        self.info_line.setCursor(QCursor(Qt.ArrowCursor))
        self.info_line.setAlignment(Qt.AlignCenter)
        self.preview_widget = QWidget(Attendance)
        self.preview_widget.setObjectName(u"preview_widget")
        self.preview_widget.setGeometry(QRect(10, 110, 640, 640))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_widget.sizePolicy().hasHeightForWidth())
        self.preview_widget.setSizePolicy(sizePolicy)
        self.attend_button = QPushButton(self.preview_widget)
        self.attend_button.setObjectName(u"attend_button")
        self.attend_button.setGeometry(QRect(250, 540, 140, 70))
        sizePolicy.setHeightForWidth(self.attend_button.sizePolicy().hasHeightForWidth())
        self.attend_button.setSizePolicy(sizePolicy)
        self.attend_button.setCheckable(True)
        self.cam_widget = QWidget(self.preview_widget)
        self.cam_widget.setObjectName(u"cam_widget")
        self.cam_widget.setGeometry(QRect(0, -1, 640, 481))
        self.recognition_widget = QWidget(Attendance)
        self.recognition_widget.setObjectName(u"recognition_widget")
        self.recognition_widget.setGeometry(QRect(710, 110, 640, 320))
        self.tittle = QLineEdit(self.recognition_widget)
        self.tittle.setObjectName(u"tittle")
        self.tittle.setGeometry(QRect(20, 10, 601, 31))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.tittle.setFont(font1)
        self.tittle.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.recognition_widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 70, 641, 251))
        self.face_preview = QHBoxLayout(self.horizontalLayoutWidget)
        self.face_preview.setSpacing(5)
        self.face_preview.setObjectName(u"face_preview")
        self.face_preview.setContentsMargins(0, 0, 0, 0)
        self.attendance_info = QWidget(Attendance)
        self.attendance_info.setObjectName(u"attendance_info")
        self.attendance_info.setGeometry(QRect(710, 430, 640, 320))
        self.attendance_table = QTableWidget(self.attendance_info)
        if (self.attendance_table.columnCount() < 4):
            self.attendance_table.setColumnCount(4)
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.attendance_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.attendance_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.attendance_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.attendance_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.attendance_table.setObjectName(u"attendance_table")
        self.attendance_table.setGeometry(QRect(0, 71, 641, 231))
        self.attendance_table.horizontalHeader().setCascadingSectionResizes(False)
        self.attendance_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.attendance_table.horizontalHeader().setStretchLastSection(True)
        self.tittle_2 = QLineEdit(self.attendance_info)
        self.tittle_2.setObjectName(u"tittle_2")
        self.tittle_2.setGeometry(QRect(20, 20, 601, 31))
        self.tittle_2.setFont(font1)
        self.tittle_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Attendance)

        QMetaObject.connectSlotsByName(Attendance)
    # setupUi

    def retranslateUi(self, Attendance):
        Attendance.setWindowTitle(QCoreApplication.translate("Attendance", u"Form", None))
        self.back_button.setText(QCoreApplication.translate("Attendance", u"Tr\u1edf l\u1ea1i", None))
        self.info_line.setText(QCoreApplication.translate("Attendance", u"Khi b\u1ea1n s\u1eb5n s\u00e0ng h\u00e3y \u1ea5n v\u00e0o n\u00fat b\u1eaft \u0111\u1ea7u \u0111\u1ec3 \u0111i\u1ec3m danh", None))
        self.attend_button.setText(QCoreApplication.translate("Attendance", u"\u0110i\u1ec3m danh", None))
        self.tittle.setText(QCoreApplication.translate("Attendance", u"Tr\u00edch xu\u1ea5t khu\u00f4n m\u1eb7t \u0111i\u1ec3m danh", None))
        ___qtablewidgetitem = self.attendance_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Attendance", u"MSSV", None));
        ___qtablewidgetitem1 = self.attendance_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Attendance", u"T\u00ean sinh vi\u00ean", None));
        ___qtablewidgetitem2 = self.attendance_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Attendance", u"Email", None));
        ___qtablewidgetitem3 = self.attendance_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Attendance", u"Th\u1eddi gian", None));
        self.tittle_2.setText(QCoreApplication.translate("Attendance", u"Th\u00f4ng tin sinh vi\u00ean \u0111\u00e3 \u0111i\u1ec3m danh", None))
    # retranslateUi

