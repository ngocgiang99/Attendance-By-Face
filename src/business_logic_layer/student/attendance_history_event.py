from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QAbstractItemView
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap
import sys
import cv2
from PySide6.QtCore import Signal, Slot, Qt, QThread
import numpy as np

from ui.student.history_view import Ui_Attendace_History
from business_logic_layer.utilities.camera_widget import CameraWidget, lock_detected_image
from business_logic_layer.database_connector.mysql_connector import MySQLConnector

class StudentHistoryWidget(Ui_Attendace_History):
    def __init__(self, logic_controller, student_info):
        super(Ui_Attendace_History, self).__init__()

        self.logic_controller = logic_controller

        # Object take from database
        self.student_info = student_info
    
    def setupUi(self, widget):
        self.main_widget = widget
        super().setupUi(widget)
        self.setup_button_click()
        self.connect_database()
        self.add_history()

        self.history_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
    
    def connect_database(self):
        self.database = MySQLConnector()

    def setup_button_click(self):
        self.back_button.clicked.connect(self.back_logged_widget)

    def back_logged_widget(self):
        self.logic_controller.show_logged_widget()

    def add_history(self):
        entries = ['one','two', 'three']

        model = QtGui.QStandardItemModel()
        self.history_view.setModel(model)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)

        mssv = self.student_info.get('mssv', 0)
        histories = self.database.get_histories(mssv)
        print(histories)
        for his in histories:
            # time = his[2].strftime("%Y-%m-%d %H:%M:%S")
            time = his[2].strftime("%H:%M:%S %d-%m-%Y-%m")

            item = QtGui.QStandardItem(time)
            item.setFont(font)
            model.appendRow(item)

        pass
