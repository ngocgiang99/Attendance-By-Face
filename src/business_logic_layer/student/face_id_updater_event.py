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
        
        QThread.sleep(2)
        
        # while True:
        #     # with lock_detected_image:
        #     lock_detected_image.lock()
        #         # print("accquire lock")
        #     if len(self.cam_viewer.detected_image) >= 30:
        #         break
        #     lock_detected_image.unlock()
        
        print("capture complete")
        self.info_line.setText(QCoreApplication.translate("FaceIdUpdater", u"Hoàn thành thu thập ảnh! Cảm ơn bạn đã sử dụng", None))
        import os
        mssv = self.student_info['mssv']
        mssv = str(mssv)
        saved_dir = os.path.join('data','face', mssv)
        if not os.path.exists(saved_dir):
            os.makedirs(saved_dir, exist_ok = True)
        
        for i, (cv_img, faces, rimg) in enumerate(self.cam_viewer.detected_image):
            # box = faces[0].bbox.astype(np.int)
            # x1,y1 = box[0]
            # x2,y2 = box[1]
            # x3,y3 = box[2]
            # x4,y4 = box[3]


            # top_left_x = min([x1,x2,x3,x4])
            # top_left_y = min([y1,y2,y3,y4])
            # bot_right_x = max([x1,x2,x3,x4])
            # bot_right_y = max([y1,y2,y3,y4])

            # cropped_image = cv_img[top_left_y:bot_right_y+1, top_left_x:bot_right_x+1]

            cropped_image = cv_img

            img_path = os.path.join(saved_dir, str(i) + ".png")
            cv2.imwrite(img_path, cropped_image)

