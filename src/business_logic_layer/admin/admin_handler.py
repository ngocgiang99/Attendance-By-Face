
from PySide6 import QtCore, QtWidgets, QtGui
import random

from business_logic_layer.admin.logged_handler import Ui_AdminWidget_Logged
from business_logic_layer.utilities.history_view_handler import AttendaceHistoryViewWidget
import cv2


class AdminHandler(object):
    def __init__(self, MainWindow, teacher_info):
        self.main_window = MainWindow
        self.teacher_info = teacher_info

    def show_widget(self, widget):
        self.centralwidget = widget
        self.main_window.setCentralWidget(widget)

    def show_logged_widget(self):
        widget = QtWidgets.QWidget(self.main_window)
        widget.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.logged_widget = Ui_AdminWidget_Logged(self, self.teacher_info)
        self.logged_widget.setupUi(widget)

        self.show_widget(widget)
        
    # def show_updater_widget(self):
    #     widget = QtWidgets.QWidget(self.main_window)
    #     widget.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))

    #     self.ui_face_id_updater = FaceIdUpdaterWidget(self, self.teacher_info)
    #     self.ui_face_id_updater.setupUi(widget)
    #     self.show_widget(widget)
    
    def show_history_widget(self):
        widget = QtWidgets.QWidget(self.main_window)
        widget.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))

        self.ui_attendance = AttendaceHistoryViewWidget(self, self.teacher_info)
        self.ui_attendance.setupUi(widget)
        self.show_widget(widget)