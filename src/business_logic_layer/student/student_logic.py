from business_logic_layer.student.face_id_updater_event import FaceIdUpdaterWidget
from business_logic_layer.student.attendance_event import AttendaceWidget
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

    def show_widget(self, widget):
        self.centralwidget = widget
        self.main_window.setCentralWidget(widget)

    def show_logged_widget(self):
        widget = QtWidgets.QWidget(self.main_window)
        widget.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.logged_widget = Ui_StudentWidget_Logged(self, self.student_info)
        self.logged_widget.setupUi(widget)

        self.show_widget(widget)
        
    def show_updater_widget(self):
        widget = QtWidgets.QWidget(self.main_window)
        widget.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))

        self.ui_face_id_updater = FaceIdUpdaterWidget(self, self.student_info)
        self.ui_face_id_updater.setupUi(widget)
        self.show_widget(widget)

    def show_attendance_widget(self):
        widget = QtWidgets.QWidget(self.main_window)
        widget.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))

        self.ui_attendance = AttendaceWidget(self, self.student_info)
        self.ui_attendance.setupUi(widget)
        self.show_widget(widget)
    