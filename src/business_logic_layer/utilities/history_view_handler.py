from PySide6 import QtCore, QtWidgets, QtGui
import random

from ui.utilities.history_view import Ui_Attendace_History
from PySide6.QtWidgets import QCalendarWidget
from PySide6.QtCore import QCoreApplication, QRect


import cv2
from datetime import datetime

class AttendaceHistoryViewWidget(Ui_Attendace_History):
    def __init__(self, logic_controller, user_info):
        super(Ui_Attendace_History, self).__init__()
        self.logic_controller = logic_controller

        # Object take from database
        self.user_info = user_info
    
    def setupUi(self, widget):
        self.main_widget = widget
        super().setupUi(widget)
        # self.loginButton.clicked.connect(self.login)
        self.setup_button_click()
        self.setup_calendar()
        

    def setup_button_click(self):
        self.back_button.clicked.connect(self.back_logged_widget)
        self.view_calendar.clicked.connect(self.view_calendar_widget)
        pass

    def back_logged_widget(self):
        self.logic_controller.show_logged_widget()
        pass

    def setup_calendar(self):
        self.calendar.clicked.connect(self.show_selected_date)
        self.calendar.hide()


    def view_calendar_widget(self):
        self.calendar.show()

    @QtCore.Slot(QtCore.QDate)
    def get_date(self, date): # <--- date parameter
        self.calendar.hide()
        date = date.toString("dd-MM-yyyy")
        self.calendar_date = datetime.strptime(date, "%d-%m-%Y")
        return self.calendar_date
        
    @QtCore.Slot(QtCore.QDate)
    def show_selected_date(self, date):
        date = self.get_date(date)
        date = date.strftime("%d-%m-%Y")
        self.date_picker.setItemText(0, QCoreApplication.translate("Attendace_History", date, None))

        pass

        