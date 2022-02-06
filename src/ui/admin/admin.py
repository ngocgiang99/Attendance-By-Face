# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget, QAbstractItemView,
    QTableWidgetItem, QWidget)

class Ui_AdminWidget(object):
    def setupUi(self, AdminWidget):
        if not AdminWidget.objectName():
            AdminWidget.setObjectName(u"AdminWidget")
        AdminWidget.resize(1366, 768)
        self.gridLayoutWidget = QWidget(AdminWidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 580, 1321, 131))
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
        self.view_attendance_history_button.setCheckable(True)

        self.utilities_button.addWidget(self.view_attendance_history_button, 0, 2, 1, 1)

        self.add_student_button = QPushButton(self.gridLayoutWidget)
        self.add_student_button.setObjectName(u"add_student_button")
        self.add_student_button.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_student_button.sizePolicy().hasHeightForWidth())
        self.add_student_button.setSizePolicy(sizePolicy1)
        self.add_student_button.setCheckable(True)

        self.utilities_button.addWidget(self.add_student_button, 0, 0, 2, 1)

        self.attendance_button = QPushButton(self.gridLayoutWidget)
        self.attendance_button.setObjectName(u"attendance_button")
        sizePolicy1.setHeightForWidth(self.attendance_button.sizePolicy().hasHeightForWidth())
        self.attendance_button.setSizePolicy(sizePolicy1)
        self.attendance_button.setCheckable(True)

        self.utilities_button.addWidget(self.attendance_button, 0, 1, 2, 1)

        self.user_info_table = QTableWidget(AdminWidget)
        if (self.user_info_table.columnCount() < 1):
            self.user_info_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.user_info_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.user_info_table.rowCount() < 2):
            self.user_info_table.setRowCount(2)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.user_info_table.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.user_info_table.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.user_info_table.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.user_info_table.setItem(1, 0, __qtablewidgetitem4)
        self.user_info_table.setObjectName(u"user_info_table")
        self.user_info_table.setGeometry(QRect(40, 140, 351, 111))
        self.user_info_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.user_info_table.horizontalHeader().setDefaultSectionSize(250)
        self.user_info_table_tittle = QLineEdit(AdminWidget)
        self.user_info_table_tittle.setObjectName(u"user_info_table_tittle")
        self.user_info_table_tittle.setGeometry(QRect(40, 70, 191, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.user_info_table_tittle.setFont(font)
        self.user_info_table_tittle.setReadOnly(True)

        self.retranslateUi(AdminWidget)

        QMetaObject.connectSlotsByName(AdminWidget)
    # setupUi

    def retranslateUi(self, AdminWidget):
        AdminWidget.setWindowTitle(QCoreApplication.translate("AdminWidget", u"Form", None))
        self.view_attendance_history_button.setText(QCoreApplication.translate("AdminWidget", u"Xem l\u1ecbch s\u1eed \u0111i\u1ec3m danh", None))
        self.add_student_button.setText(QCoreApplication.translate("AdminWidget", u"Th\u00eam sinh vi\u00ean", None))
        self.attendance_button.setText(QCoreApplication.translate("AdminWidget", u"\u0110i\u1ec3m danh", None))
        ___qtablewidgetitem = self.user_info_table.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdminWidget", u"T\u00ean qu\u1ea3n tr\u1ecb vi\u00ean:", None));
        ___qtablewidgetitem1 = self.user_info_table.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdminWidget", u"Email:", None));

        __sortingEnabled = self.user_info_table.isSortingEnabled()
        self.user_info_table.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.user_info_table.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdminWidget", u"Tr\u01b0\u01a1ng Ng\u1ecdc Giang", None));
        ___qtablewidgetitem3 = self.user_info_table.item(1, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdminWidget", u"giangtn.170067@sis.hust.edu.vn", None));
        self.user_info_table.setSortingEnabled(__sortingEnabled)

        self.user_info_table_tittle.setText(QCoreApplication.translate("AdminWidget", u"Th\u00f4ng tin qu\u1ea3n tr\u1ecb vi\u00ean", None))
    # retranslateUi

