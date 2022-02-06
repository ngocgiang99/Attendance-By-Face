from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QCoreApplication
import random

from ui.teacher.teacher import Ui_TeacherWidget

import cv2

class Ui_TeacherWidget_Logged(Ui_TeacherWidget):
    def __init__(self, logic_controller, teacher_info):
        super(Ui_TeacherWidget, self).__init__()
        self.logic_controller = logic_controller

        # Object take from database
        self.teacher_info = teacher_info
    
    def setupUi(self, widget):
        self.main_widget = widget
        super().setupUi(widget)
        # self.loginButton.clicked.connect(self.login)
        self.setup_table_info()
        self.setup_button_click()
        print('setup student login')
        

    def setup_table_info(self):
        student_name = self.teacher_info.get('name', "error")
        email = self.teacher_info.get('email', 'error@')



        self.user_info_table.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.user_info_table.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TeacherWidget", student_name, None));
        ___qtablewidgetitem5 = self.user_info_table.item(1, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TeacherWidget", email, None));
        pass

    def setup_button_click(self):
        # self.update_face_id_button.clicked.connect(self.update_face_id)
        self.update_face_id_button.hide()
        self.attendance_button.clicked.connect(self.take_attendace)
        self.view_attendance_history_button.clicked.connect(self.view_history_attendace)
        self.logout_button.clicked.connect(self.logout)


    def take_attendace(self):
        self.logic_controller.show_attendance_widget()

    def view_history_attendace(self):
        self.logic_controller.show_history_widget()

    def logout(self):
        self.logic_controller.logout()

        