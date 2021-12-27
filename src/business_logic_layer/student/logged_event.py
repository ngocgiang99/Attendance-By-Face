from business_logic_layer.student.face_id_updater_event import FaceIdUpdaterWidget
from ui.student.faceid_updater import Ui_FaceIdUpdater
from ui.student.student import Ui_StudentWidget
from PySide6 import QtCore, QtWidgets, QtGui
import random

from ui.student.student import Ui_StudentWidget

import cv2

class Ui_StudentWidget_Logged(Ui_StudentWidget):
    def __init__(self, logic_controller, student_info):
        super(Ui_StudentWidget, self).__init__()
        self.logic_controller = logic_controller

        # Object take from database
        self.student_info = student_info
    
    def setupUi(self, widget):
        self.main_widget = widget
        super().setupUi(widget)
        # self.loginButton.clicked.connect(self.login)
        self.setup_table_info()
        self.setup_button_click()
        print('setup student login')
        

    def setup_table_info(self):
        pass

    def setup_button_click(self):
        self.update_face_id_button.clicked.connect(self.update_face_id)
        self.attendance_button.clicked.connect(self.take_attendace)
        self.view_attendance_history_button.clicked.connect(self.view_history_attendace)

    def update_face_id(self):
        self.logic_controller.show_updater_widget()



    def take_attendace(self):
        pass

    def view_history_attendace(self):
        pass

        