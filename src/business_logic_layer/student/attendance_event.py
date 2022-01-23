from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap
import sys
import cv2
from PySide6.QtCore import Signal, Slot, Qt, QThread
import numpy as np

from ui.student.attendance import Ui_Attendance
from business_logic_layer.utilities.camera_widget import CameraWidget, lock_detected_image


class AttendaceWidget(Ui_Attendance):
    def __init__(self, logic_controller, student_info):
        super(Ui_Attendance, self).__init__()

        self.logic_controller = logic_controller

        # Object take from database
        self.student_info = student_info
    
    def setupUi(self, widget):
        self.main_widget = widget
        super().setupUi(widget)
        self.setup_cam_viewer()
        self.setup_button_click()
        

    def setup_cam_viewer(self):
        self.cam_viewer = CameraWidget(self.cam_widget)
        # self.cam_viewer.show()



    def setup_button_click(self):
        self.back_button.clicked.connect(self.back_logged_widget)
        self.attend_button.clicked.connect(self.attend)
        pass

    def back_logged_widget(self):
        self.cam_viewer.close()
        self.logic_controller.show_logged_widget()
        pass

    def attend(self):
        pass