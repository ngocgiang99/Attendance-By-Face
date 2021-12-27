from ui.started_window.started_window import Ui_MainWindow
from PySide6 import QtCore, QtWidgets, QtGui
import random

from business_logic_layer.student.student_logic import StudentLogic

class Ui_MainWindow_Show(Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
    
    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        super().setupUi(MainWindow)
        self.loginButton.clicked.connect(self.login)
        self.main_window.setWindowTitle('Login')

    def login(self):
                
        # database
        database = None

        # Get user information from database
        username = self.username.toPlainText()
        print(username)
        password = self.password.toPlainText()
        print(password)
        
        if database is not None:
            user_info = database.get_user_info(username, password)
        else:
            user_info = None

        # Check type of user
        user_type = 0

        # Move to alternative widget with user type 
        if (user_type == 0):
            self.student_widget = StudentLogic(self.main_window, user_info)
            self.student_widget.show_logged_widget()
            
        elif user_type == 1:
            # Teacher user
            pass
        else:
            # Adminstration user
            pass
        # self.centralwidget = widget
        # self.main_window.setCentralWidget(widget)


        
