from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QCoreApplication
import random
from PySide6.QtWidgets import  QDialog

from ui.admin.student_form import Ui_student_form

import cv2

class StudentForm(QDialog, Ui_student_form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

    def pop_up_student_form(self):
        
        pass

    @staticmethod
    def get_student_info(parent = None):
        dialog = StudentForm(parent)
        result = dialog.exec_()
        email = dialog.email_line_edit.text()
        mssv = dialog.mssv_line_edit.text()
        mssv = int(mssv)
        student_name = dialog.student_name_line_edit.text()
        return (email, mssv, student_name, result == QDialog.Accepted)

    
        