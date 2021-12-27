from ui.student.faceid_updater import Ui_FaceIdUpdater
from ui.student.student import Ui_StudentWidget
from PySide6 import QtCore, QtWidgets, QtGui
import random

from ui.student.student import Ui_StudentWidget
from business_logic_layer.student.logged_event import Ui_StudentWidget_Logged
import cv2


class StudentLogic(object):
    def __init__(self, MainWindow, student_info):
        self.main_window = MainWindow
        self.student_info = student_info

    def show_logged_widget(self):
        widget = QtWidgets.QWidget(self.main_window)
        widget.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.logged_widget = Ui_StudentWidget_Logged(self.student_info)
        self.logged_widget.setupUi(widget)
        
        self.centralwidget = widget
        self.main_window.setCentralWidget(widget)

    