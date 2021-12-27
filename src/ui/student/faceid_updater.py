# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_face.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_FaceIdUpdater(object):
    def setupUi(self, FaceIdUpdater):
        if not FaceIdUpdater.objectName():
            FaceIdUpdater.setObjectName(u"FaceIdUpdater")
        FaceIdUpdater.resize(1366, 768)
        self.back_button = QPushButton(FaceIdUpdater)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(20, 20, 91, 31))
        self.back_button.setCheckable(True)
        self.info_line = QLineEdit(FaceIdUpdater)
        self.info_line.setObjectName(u"info_line")
        self.info_line.setGeometry(QRect(160, 21, 1171, 61))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        self.info_line.setFont(font)
        self.info_line.setCursor(QCursor(Qt.ArrowCursor))
        self.info_line.setAlignment(Qt.AlignCenter)
        self.start_capture_image_button = QPushButton(FaceIdUpdater)
        self.start_capture_image_button.setObjectName(u"start_capture_image_button")
        self.start_capture_image_button.setGeometry(QRect(10, 170, 129, 69))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_capture_image_button.sizePolicy().hasHeightForWidth())
        self.start_capture_image_button.setSizePolicy(sizePolicy)
        self.start_capture_image_button.setCheckable(True)
        self.cam_widget = QWidget(FaceIdUpdater)
        self.cam_widget.setObjectName(u"cam_widget")
        self.cam_widget.setGeometry(QRect(159, 133, 1171, 601))
        sizePolicy.setHeightForWidth(self.cam_widget.sizePolicy().hasHeightForWidth())
        self.cam_widget.setSizePolicy(sizePolicy)

        self.retranslateUi(FaceIdUpdater)

        QMetaObject.connectSlotsByName(FaceIdUpdater)
    # setupUi

    def retranslateUi(self, FaceIdUpdater):
        FaceIdUpdater.setWindowTitle(QCoreApplication.translate("FaceIdUpdater", u"Form", None))
        self.back_button.setText(QCoreApplication.translate("FaceIdUpdater", u"Tr\u1edf l\u1ea1i", None))
        self.info_line.setText(QCoreApplication.translate("FaceIdUpdater", u"Khi b\u1ea1n s\u1eb5n s\u00e0ng h\u00e3y \u1ea5n v\u00e0o n\u00fat b\u1eaft \u0111\u1ea7u \u0111\u1ec3 thu th\u1eadp \u1ea3nh", None))
        self.start_capture_image_button.setText(QCoreApplication.translate("FaceIdUpdater", u"B\u1eaft \u0111\u1ea7u l\u1ea5y \u1ea3nh", None))
    # retranslateUi

