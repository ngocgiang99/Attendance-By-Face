from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap
import sys
import cv2
from PySide6.QtCore import Signal, Slot, Qt, QThread
import numpy as np

from ui.teacher.attendance import Ui_Attendance

class AttendanceWidget(Ui_Attendance):
    def __init__(self, logic_controller, teacher_info):
        super(Ui_Attendance, self).__init__()

        self.logic_controller = logic_controller

        # Object take from database
        self.teacher_info = teacher_info
    
    def setupUi(self, widget):
        self.main_widget = widget
        super().setupUi(widget)
        self.setup_button_click()
        self.setup_preview_widget()

    def setup_button_click(self):
        self.back_button.clicked.connect(self.back_logged_widget)
        self.attend_button.clicked.connect(self.attend)
        pass

    def back_logged_widget(self):
        self.logic_controller.show_logged_widget()
        pass

    def setup_table_view(self):
        self.attendance_table.horizontalHeader().setStretchLastSection(True) 
        self.attendance_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        pass
    
    def setup_preview_widget(self):
        pass

    def attend(self):
        pass

