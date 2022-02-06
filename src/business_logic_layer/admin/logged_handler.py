from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import  QDialog
import random

from ui.admin.admin import Ui_AdminWidget
from business_logic_layer.admin.student_form_handler import StudentForm
from business_logic_layer.database_connector.mysql_connector import MySQLConnector

import cv2

class Ui_AdminWidget_Logged(Ui_AdminWidget):
    def __init__(self, logic_controller, admin_info):
        super(Ui_AdminWidget, self).__init__()
        self.logic_controller = logic_controller

        # Object take from database
        self.admin_info = admin_info
    
    def setupUi(self, widget):
        self.main_widget = widget
        super().setupUi(widget)
        # self.loginButton.clicked.connect(self.login)
        self.setup_table_info()
        self.setup_button_click()
        self.setup_database()
        print('setup student login')
        

    def setup_table_info(self):
        user_name = self.admin_info.get('name', "error")
        email = self.admin_info.get('email', 'error@')



        self.user_info_table.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.user_info_table.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdminWidget", user_name, None));
        ___qtablewidgetitem5 = self.user_info_table.item(1, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AdminWidget", email, None));
        pass

    def setup_button_click(self):
        self.attendance_button.hide()
        self.add_student_button.clicked.connect(self.pop_up_student_form)
        self.view_attendance_history_button.clicked.connect(self.view_history_attendace)
        self.logout_button.clicked.connect(self.logout)

    def setup_database(self):
        self.db_connector = MySQLConnector()

    def view_history_attendace(self):
        self.logic_controller.show_history_widget()

    def pop_up_student_form(self):
        email, mssv, student_name, status = StudentForm.get_student_info()
        if status == QDialog.Accepted:
            print(email, mssv, student_name)
        else:
            print('not have any info')

        pwd = '123456'
        self.db_connector.insert_new_student(email, mssv, student_name, pwd)

        pass
    
    def logout(self):
        self.logic_controller.logout()