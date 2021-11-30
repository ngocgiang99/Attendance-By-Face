import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from main_show import Ui_MainWindow_Show



if __name__ == "__main__":
    app = QtWidgets.QApplication()
    # create window
    window = QtWidgets.QMainWindow()

    ui = Ui_MainWindow_Show()
    # fill window
    ui.setupUi(window)

    window.show()

    # widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()
    # window.setCentralWidget(widget)
    

    sys.exit(app.exec_())