from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap
import sys
import os
import cv2
from PySide6.QtCore import Signal, Slot, Qt, QThread
import numpy as np

from ui.student.attendance import Ui_Attendance
from business_logic_layer.utilities.camera_widget import CameraWidget, lock_detected_image
from ml_services.api.face_recognition.face_recognition_arcface import ArcFaceSingleton

from business_logic_layer.utilities.similarity_function import cosine_similarity, COSINE_THRESHOLD
from business_logic_layer.database_connector.mysql_connector import MySQLConnector
class AttendaceWidget(Ui_Attendance):
    def __init__(self, logic_controller, student_info):
        super(Ui_Attendance, self).__init__()

        self.logic_controller = logic_controller

        # Object take from database
        self.student_info = student_info
    
    def setupUi(self, widget):
        self.main_widget = widget
        super().setupUi(widget)
        self.setup_cam_viewer()
        self.setup_button_click()
        self.setup_ml_services()
        self.connect_database()
        

    def setup_cam_viewer(self):
        self.cam_viewer = CameraWidget(self.cam_widget)
        # self.cam_viewer.show()

    def connect_database(self):
        self.database = MySQLConnector()

    def setup_ml_services(self):
        model_pack_name = 'buffalo_m'
        root = 'ml_services/data/model'
        self.recognition = ArcFaceSingleton(root, model_pack_name, providers=[ 'CPUExecutionProvider'])
        self.recognition.prepare(ctx_id=0, det_size=(480, 640))

    def setup_button_click(self):
        self.back_button.clicked.connect(self.back_logged_widget)
        self.attend_button.clicked.connect(self.attend)
        pass

    def back_logged_widget(self):
        self.cam_viewer.close()
        self.logic_controller.show_logged_widget()
        pass

    def attend_fail(self):
        self.info_line.setText(QCoreApplication.translate("Attendance", u"Điểm danh thất bại, xin hãy điểm danh lại!", None))

        return None

    def attend_success(self):
        self.info_line.setText(QCoreApplication.translate("Attendance", u"Điểm danh thành công!", None))
        mssv = self.student_info.get('mssv', 0)
        self.database.insert_attendance(mssv)
        return None

    def attend(self):


        # get image from cam
        self.cam_viewer.capture_image(1)
        if len(self.cam_viewer.detected_image) == 0:
            
            return self.attend_fail()
        (img, _, _) = self.cam_viewer.detected_image[0]
        h,w,_ = img.shape
        # cv2.imshow("test", img)
        # print("capture done")

        # get image from database
        mssv = self.student_info.get('mssv', 0)
        database_dir = os.path.join('data/face', str(mssv))
        db_img = []
        for _, _, filenames in os.walk(database_dir):
            for filename in filenames:
                img_path = os.path.join(database_dir, filename)
                db_img.append(cv2.imread(img_path))

        print('number comparable image:', len(db_img))


        faces = self.recognition.get(img)
        rimg = self.recognition.draw_on(img, faces)

        # cv2.imshow("cap image", rimg)
        print(faces[0]['embedding'].shape)
        print(type(faces[0]['embedding']))

        face = faces[0]

        sim = 0
        for t_img in db_img:
            t_faces = self.recognition.get(img)
            t_face = faces[0]

            cos_sim = cosine_similarity(face['embedding'], t_face['embedding'])
            sim += cos_sim

        print("similarity: ", sim)
        if sim < COSINE_THRESHOLD:
            self.attend_success()
        else:
            return self.attend_fail()
        # cv2.waitKey(0)
        
