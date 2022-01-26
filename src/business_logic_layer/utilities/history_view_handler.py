from PySide6 import QtCore, QtWidgets, QtGui
import random

from ui.utilities.history_view import Ui_Attendace_History
from business_logic_layer.database_connector.mysql_connector import MySQLConnector
from PySide6.QtWidgets import QCalendarWidget, QTableWidgetItem
from PySide6.QtCore import QCoreApplication, QRect


import cv2
import datetime

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
        self.search_button.clicked.connect(self.view_history)
        self.export_res_button.clicked.connect(self.export_res)
        pass

    def back_logged_widget(self):
        self.logic_controller.show_logged_widget()
        pass

    def setup_calendar(self):
        self.calendar.clicked.connect(self.show_selected_date)
        self.calendar.hide()


    def view_calendar_widget(self):
        self.calendar.show()
        self.calendar.raise_()

    @QtCore.Slot(QtCore.QDate)
    def get_date(self, date): # <--- date parameter
        self.calendar.hide()
        date = date.toString("dd-MM-yyyy")
        self.calendar_date = datetime.datetime.strptime(date, "%d-%m-%Y")
        return self.calendar_date
        
    @QtCore.Slot(QtCore.QDate)
    def show_selected_date(self, date):
        date = self.get_date(date)
        date = date.strftime("%d-%m-%Y")
        if self.date_picker.count() == 0:
            self.date_picker.addItem("")
        self.date_picker.setItemText(0, QCoreApplication.translate("Attendace_History", date, None))

        pass

    def view_history(self):
        connector = MySQLConnector()
        date_start = self.calendar_date
        date_end = date_start + datetime.timedelta(days=1)
        print(date_start)
        print(date_end)

        histories = connector.get_his_between_time(date_start, date_end)
        print(histories)

        for his in histories:
            # time = his[2].strftime("%Y-%m-%d %H:%M:%S")
            time = his[2].strftime("%H:%M:%S %d-%m-%Y-%m")
            mssv = int(his[1])
            student_info = connector.get_student_info(mssv)

            student_name = student_info['name']
            student_email = student_info['email']
            time_attend = time
            mssv = str(mssv)

            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition , 0, QTableWidgetItem(mssv))
            self.tableWidget.setItem(rowPosition , 1, QTableWidgetItem(student_name))
            self.tableWidget.setItem(rowPosition , 2, QTableWidgetItem(student_email))
            self.tableWidget.setItem(rowPosition , 3, QTableWidgetItem(time_attend))
            

        pass

    def export_res(self):
        pass

        