from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
import sys
import cv2
from PySide6.QtCore import Signal, Slot, Qt, QThread
import numpy as np

from ui.student.faceid_updater import Ui_FaceIdUpdater
from business_logic_layer.utilities.camera_widget import CameraWidget


class FaceIdUpdaterWidget(Ui_FaceIdUpdater):
    def __init__(self, logic_controller, student_info):
        super(Ui_FaceIdUpdater, self).__init__()

        self.logic_controller = logic_controller

        # Object take from database
        self.student_info = student_info
    
    def setupUi(self, widget):
        self.main_widget = widget
        super().setupUi(widget)
        self.setup_cam_viewer()
        self.setup_button_click()
        

    def setup_cam_viewer(self):
        # widget = QWidget(self.camera_widget)
        self.cam_viewer = CameraWidget(self.cam_widget)
        self.cam_viewer.show()
        # self.cam_widget = cam_viewer

        # self.cam_widget.show()


    def setup_button_click(self):
        self.back_button.clicked.connect(self.back_logged_widget)
        self.start_capture_image_button.clicked.connect(self.capture_image)
        pass

    def back_logged_widget(self):
        self.cam_viewer.close()
        self.logic_controller.show_logged_widget()
        pass

    def capture_image(self):
        pass