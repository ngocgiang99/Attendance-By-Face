from ui.started_window.started_window import Ui_MainWindow
from PySide6 import QtCore, QtWidgets, QtGui
import random

from business_logic_layer.student.student_window_event import Ui_StudentWidget_Show

class Ui_MainWindow_Show(Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
    
    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        super().setupUi(MainWindow)
        self.loginButton.clicked.connect(self.login)

    def login(self):
        widget = QtWidgets.QWidget()
        student_widget = Ui_StudentWidget_Show()
        student_widget.setupUi(widget)
        self.main_window.setCentralWidget(widget)
