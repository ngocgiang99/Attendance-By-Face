from ui.started_window.started_window import Ui_MainWindow
from PySide6 import QtCore, QtWidgets, QtGui
import random

from business_logic_layer.student.student_logic import StudentLogic
from business_logic_layer.teacher.teacher_handler import TeacherHandler
from business_logic_layer.admin.admin_handler import AdminHandler
from business_logic_layer.database_connector.mysql_connector import MySQLConnector
class Ui_MainWindow_Show(Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
    
    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        super().setupUi(MainWindow)
        self.loginButton.clicked.connect(self.login)
        self.main_window.setWindowTitle('Login')
        self.connect_database()

    def connect_database(self):
        self.database = MySQLConnector()
        


    def login(self):
                
        # database
        database = None

        # Get user information from database
        username = self.username.toPlainText()
        print(username)
        password = self.password.toPlainText()
        print(password)
        
        if self.database is not None:
            user_info = self.database.get_user_info(username, password)
        else:
            user_info = None

        if user_info is None:
            print("Wrong username or password!")
            return None

        # Check type of user
        user_type = 2

        # Move to alternative widget with user type 
        if (user_type == 0):
            self.student_widget = StudentLogic(self.main_window, user_info)
            self.student_widget.show_logged_widget()
            
        elif user_type == 1:
            # Teacher user
            self.teacher_widget = TeacherHandler(self.main_window, user_info)
            self.teacher_widget.show_logged_widget()
            pass
        else:
            # Adminstration user
            self.admin_widget = AdminHandler(self.main_window, user_info)
            self.admin_widget.show_logged_widget()
            pass
        # self.centralwidget = widget
        # self.main_window.setCentralWidget(widget)


        
