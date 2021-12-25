# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_StudentWidget(object):
    def setupUi(self, StudentWidget):
        if not StudentWidget.objectName():
            StudentWidget.setObjectName(u"StudentWidget")
        StudentWidget.resize(1389, 792)
        self.gridLayoutWidget = QWidget(StudentWidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 580, 1321, 131))
        self.utilities_button = QGridLayout(self.gridLayoutWidget)
        self.utilities_button.setObjectName(u"utilities_button")
        self.utilities_button.setSizeConstraint(QLayout.SetMaximumSize)
        self.utilities_button.setHorizontalSpacing(1)
        self.utilities_button.setVerticalSpacing(3)
        self.utilities_button.setContentsMargins(0, 0, 0, 0)
        self.view_attendance_history_button = QPushButton(self.gridLayoutWidget)
        self.view_attendance_history_button.setObjectName(u"view_attendance_history_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_attendance_history_button.sizePolicy().hasHeightForWidth())
        self.view_attendance_history_button.setSizePolicy(sizePolicy)

        self.utilities_button.addWidget(self.view_attendance_history_button, 0, 2, 1, 1)

        self.update_face_id_button = QPushButton(self.gridLayoutWidget)
        self.update_face_id_button.setObjectName(u"update_face_id_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.update_face_id_button.sizePolicy().hasHeightForWidth())
        self.update_face_id_button.setSizePolicy(sizePolicy1)

        self.utilities_button.addWidget(self.update_face_id_button, 0, 0, 2, 1)

        self.attendance_button = QPushButton(self.gridLayoutWidget)
        self.attendance_button.setObjectName(u"attendance_button")
        sizePolicy1.setHeightForWidth(self.attendance_button.sizePolicy().hasHeightForWidth())
        self.attendance_button.setSizePolicy(sizePolicy1)

        self.utilities_button.addWidget(self.attendance_button, 0, 1, 2, 1)

        self.user_info_table = QTableWidget(StudentWidget)
        if (self.user_info_table.columnCount() < 1):
            self.user_info_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.user_info_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.user_info_table.rowCount() < 3):
            self.user_info_table.setRowCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.user_info_table.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.user_info_table.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.user_info_table.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.user_info_table.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.user_info_table.setItem(1, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.user_info_table.setItem(2, 0, __qtablewidgetitem6)
        self.user_info_table.setObjectName(u"user_info_table")
        self.user_info_table.setGeometry(QRect(40, 140, 351, 111))
        self.user_info_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.user_info_table.horizontalHeader().setDefaultSectionSize(250)
        self.user_info_table_tittle = QLineEdit(StudentWidget)
        self.user_info_table_tittle.setObjectName(u"user_info_table_tittle")
        self.user_info_table_tittle.setGeometry(QRect(40, 70, 191, 31))
        font = QFont()
        font.setFamilies([u"DejaVu Sans"])
        font.setPointSize(12)
        font.setBold(True)
        self.user_info_table_tittle.setFont(font)
        self.user_info_table_tittle.setReadOnly(True)

        self.retranslateUi(StudentWidget)

        QMetaObject.connectSlotsByName(StudentWidget)
    # setupUi

    def retranslateUi(self, StudentWidget):
        StudentWidget.setWindowTitle(QCoreApplication.translate("StudentWidget", u"Form", None))
        self.view_attendance_history_button.setText(QCoreApplication.translate("StudentWidget", u"Xem l\u1ecbch s\u1eed \u0111i\u1ec3m danh", None))
        self.update_face_id_button.setText(QCoreApplication.translate("StudentWidget", u"C\u1eadp nh\u1eadt khu\u00f4n m\u1eb7t", None))
        self.attendance_button.setText(QCoreApplication.translate("StudentWidget", u"\u0110i\u1ec3m danh", None))
        ___qtablewidgetitem = self.user_info_table.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StudentWidget", u"T\u00ean sinh vi\u00ean:", None));
        ___qtablewidgetitem1 = self.user_info_table.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StudentWidget", u"MSSV:", None));
        ___qtablewidgetitem2 = self.user_info_table.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StudentWidget", u"Email:", None));

        __sortingEnabled = self.user_info_table.isSortingEnabled()
        self.user_info_table.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.user_info_table.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("StudentWidget", u"Tr\u01b0\u01a1ng Ng\u1ecdc Giang", None));
        ___qtablewidgetitem4 = self.user_info_table.item(1, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("StudentWidget", u"20170067", None));
        ___qtablewidgetitem5 = self.user_info_table.item(2, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("StudentWidget", u"giangtn.170067@sis.hust.edu.vn", None));
        self.user_info_table.setSortingEnabled(__sortingEnabled)

        self.user_info_table_tittle.setText(QCoreApplication.translate("StudentWidget", u"Th\u00f4ng Tin sinh vi\u00ean", None))
    # retranslateUi

