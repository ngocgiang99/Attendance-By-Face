from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
import sys
import cv2
from PySide6.QtCore import Signal, Slot, Qt, QThread
import numpy as np

from ui.student.faceid_updater import Ui_FaceIdUpdater
from business_logic_layer.student.face_id_updater_event import CameraWidget


class FaceIdUpdaterWidget(Ui_FaceIdUpdater):
    def __init__(self, student_info):
        super(Ui_FaceIdUpdater, self).__init__()

        # Object take from database
        self.student_info = student_info
    
    def setupUi(self, widget):
        self.main_widget = widget
        super().setupUi(widget)
        self.setup_cam_viewer()
        self.setup_button_click()
        

    def setup_cam_viewer(self):
        cam_viewer = CameraWidget()
        self.cam_widget = cam_viewer


    def setup_button_click(self):
        pass