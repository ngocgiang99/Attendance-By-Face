from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap
import sys
import cv2
from PySide6.QtCore import Signal, Slot, Qt, QThread
import numpy as np

from ui.student.faceid_updater import Ui_FaceIdUpdater
from business_logic_layer.utilities.camera_widget import CameraWidget, lock_detected_image

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
        self.cam_viewer = CameraWidget(self.cam_widget)
        # self.cam_viewer.show()



    def setup_button_click(self):
        self.back_button.clicked.connect(self.back_logged_widget)
        self.start_capture_image_button.clicked.connect(self.capture_image)
        pass

    def back_logged_widget(self):
        self.cam_viewer.close()
        self.logic_controller.show_logged_widget()
        pass

    def capture_image(self):
        self.info_line.setText(QCoreApplication.translate("FaceIdUpdater", u"Bắt đầu thu thập ảnh...", None))
        self.cam_viewer.capture_image()
        
        QThread.sleep(5)
        # import time
        # time.sleep(5)
        # while True:
        #     # lock_detected_image.acquire()
        #     lock_detected_image.lock()
        #     print('lock 1')
        #     print("test len ", len(self.cam_viewer.detected_image))
        #     if len(self.cam_viewer.detected_image) >= 30:
        #         break
        #     # lock_detected_image.release()
        #     lock_detected_image.unlock()
        #     print('release 1')
        #     # time.sleep(5)
        #     QThread.sleep(5)

        self.info_line.setText(QCoreApplication.translate("FaceIdUpdater", u"Hoàn thành thu thập ảnh! Cảm ơn bạn đã sử dụng", None))