# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'started_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1367, 768)
        MainWindow.setLocale(QLocale(QLocale.Vietnamese, QLocale.Vietnam))
        self.actionT_c_gi_Tr_ng_Ng_c_Giang = QAction(MainWindow)
        self.actionT_c_gi_Tr_ng_Ng_c_Giang.setObjectName(u"actionT_c_gi_Tr_ng_Ng_c_Giang")
        self.actionemail_truongngocgiang99_gmail_com = QAction(MainWindow)
        self.actionemail_truongngocgiang99_gmail_com.setObjectName(u"actionemail_truongngocgiang99_gmail_com")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLocale(QLocale(QLocale.Vietnamese, QLocale.Vietnam))
        self.LoginWidget = QWidget(self.centralwidget)
        self.LoginWidget.setObjectName(u"LoginWidget")
        self.LoginWidget.setGeometry(QRect(480, 170, 320, 200))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginWidget.sizePolicy().hasHeightForWidth())
        self.LoginWidget.setSizePolicy(sizePolicy)
        self.LoginWidget.setLocale(QLocale(QLocale.Vietnamese, QLocale.Vietnam))
        self.labelWidget = QLabel(self.LoginWidget)
        self.labelWidget.setObjectName(u"labelWidget")
        self.labelWidget.setGeometry(QRect(120, 10, 72, 20))
        sizePolicy.setHeightForWidth(self.labelWidget.sizePolicy().hasHeightForWidth())
        self.labelWidget.setSizePolicy(sizePolicy)
        self.labelWidget.setLocale(QLocale(QLocale.Vietnamese, QLocale.Vietnam))
        self.labelWidget.setAlignment(Qt.AlignCenter)
        self.username = QTextEdit(self.LoginWidget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(20, 50, 281, 31))
        self.username.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.password = QTextEdit(self.LoginWidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(20, 110, 281, 31))
        self.password.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.loginButton = QPushButton(self.LoginWidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setEnabled(True)
        self.loginButton.setGeometry(QRect(20, 160, 75, 25))
        self.loginButton.setCheckable(True)
        self.loginButton.setChecked(False)
        self.loginButton.setAutoDefault(False)
        self.loginButton.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1367, 22))
        self.menuAbout_me = QMenu(self.menubar)
        self.menuAbout_me.setObjectName(u"menuAbout_me")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout_me.menuAction())
        self.menuAbout_me.addAction(self.actionT_c_gi_Tr_ng_Ng_c_Giang)
        self.menuAbout_me.addAction(self.actionemail_truongngocgiang99_gmail_com)

        self.retranslateUi(MainWindow)

        self.loginButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionT_c_gi_Tr_ng_Ng_c_Giang.setText(QCoreApplication.translate("MainWindow", u"T\u00ean: Tr\u01b0\u01a1ng Ng\u1ecdc Giang", None))
        self.actionemail_truongngocgiang99_gmail_com.setText(QCoreApplication.translate("MainWindow", u"Email: truongngocgiang99@gmail.com", None))
#if QT_CONFIG(whatsthis)
        self.LoginWidget.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.labelWidget.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng nh\u1eadp", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng nh\u1eadp", None))
        self.menuAbout_me.setTitle(QCoreApplication.translate("MainWindow", u"About me", None))
    # retranslateUi

