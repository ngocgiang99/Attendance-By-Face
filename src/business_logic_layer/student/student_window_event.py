from ui.student.student import Ui_StudentWidget
from PySide6 import QtCore, QtWidgets, QtGui
import random

from ui.student.student import Ui_StudentWidget

class Ui_StudentWidget_Show(Ui_StudentWidget):
    def __init__(self):
        super(Ui_StudentWidget, self).__init__()
    
    def setupUi(self, widget):
        self.main_widget = widget
        super().setupUi(widget)
        # self.loginButton.clicked.connect(self.login)