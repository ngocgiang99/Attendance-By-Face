# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student_form.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_student_form(object):
    def setupUi(self, student_form):
        if not student_form.objectName():
            student_form.setObjectName(u"student_form")
        student_form.resize(427, 283)
        self.gridLayout = QGridLayout(student_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.email_label = QLabel(student_form)
        self.email_label.setObjectName(u"email_label")

        self.gridLayout_2.addWidget(self.email_label, 0, 0, 1, 1)

        self.email_line_edit = QLineEdit(student_form)
        self.email_line_edit.setObjectName(u"email_line_edit")

        self.gridLayout_2.addWidget(self.email_line_edit, 0, 1, 1, 1)

        self.mssv_label = QLabel(student_form)
        self.mssv_label.setObjectName(u"mssv_label")

        self.gridLayout_2.addWidget(self.mssv_label, 1, 0, 1, 1)

        self.mssv_line_edit = QLineEdit(student_form)
        self.mssv_line_edit.setObjectName(u"mssv_line_edit")

        self.gridLayout_2.addWidget(self.mssv_line_edit, 1, 1, 1, 1)

        self.student_name_label = QLabel(student_form)
        self.student_name_label.setObjectName(u"student_name_label")

        self.gridLayout_2.addWidget(self.student_name_label, 2, 0, 1, 1)

        self.student_name_line_edit = QLineEdit(student_form)
        self.student_name_line_edit.setObjectName(u"student_name_line_edit")

        self.gridLayout_2.addWidget(self.student_name_line_edit, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(student_form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(student_form)
        self.buttonBox.accepted.connect(student_form.accept)
        self.buttonBox.rejected.connect(student_form.reject)

        QMetaObject.connectSlotsByName(student_form)
    # setupUi

    def retranslateUi(self, student_form):
        student_form.setWindowTitle(QCoreApplication.translate("student_form", u"Dialog", None))
        self.email_label.setText(QCoreApplication.translate("student_form", u"Email:", None))
        self.mssv_label.setText(QCoreApplication.translate("student_form", u"MSSV:", None))
        self.student_name_label.setText(QCoreApplication.translate("student_form", u"T\u00ean sinh vi\u00ean", None))
    # retranslateUi

