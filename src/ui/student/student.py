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
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextBrowser, QWidget)

class Ui_StudentWidget(object):
    def setupUi(self, StudentWidget):
        if not StudentWidget.objectName():
            StudentWidget.setObjectName(u"StudentWidget")
        StudentWidget.resize(1389, 792)
        self.gridLayoutWidget = QWidget(StudentWidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 580, 1321, 131))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 2, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 2, 1)

        self.textBrowser = QTextBrowser(StudentWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(40, 90, 181, 21))
        self.tableWidget = QTableWidget(StudentWidget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 140, 261, 111))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)

        self.retranslateUi(StudentWidget)

        QMetaObject.connectSlotsByName(StudentWidget)
    # setupUi

    def retranslateUi(self, StudentWidget):
        StudentWidget.setWindowTitle(QCoreApplication.translate("StudentWidget", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("StudentWidget", u"Xem l\u1ecbch s\u1eed \u0111i\u1ec3m danh", None))
        self.pushButton.setText(QCoreApplication.translate("StudentWidget", u"C\u1eadp nh\u1eadt khu\u00f4n m\u1eb7t", None))
        self.pushButton_3.setText(QCoreApplication.translate("StudentWidget", u"\u0110i\u1ec3m danh", None))
        self.textBrowser.setHtml(QCoreApplication.translate("StudentWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#ff5500;\">Th\u00f4ng Tin sinh vi\u00ean</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StudentWidget", u"T\u00ean sinh vi\u00ean:", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StudentWidget", u"MSSV:", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StudentWidget", u"Email:", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("StudentWidget", u"Tr\u01b0\u01a1ng Ng\u1ecdc Giang", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

