from ui.started_window.main import Ui_MainWindow
from PySide6 import QtCore, QtWidgets, QtGui
import random
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

class Ui_MainWindow_Show(Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
    
    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        super().setupUi(MainWindow)
        self.loginButton.clicked.connect(self.login)

    def login(self):
        widget = MyWidget()
        self.main_window.setCentralWidget(widget)

