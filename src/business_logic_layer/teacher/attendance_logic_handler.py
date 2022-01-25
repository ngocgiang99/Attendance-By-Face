from PySide6 import QtGui
from PySide6.QtWidgets import QSizePolicy, QWidget, QApplication, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
import sys
import cv2
from PySide6.QtCore import QRect, Signal, Slot, Qt, QThread, QMutex
import numpy as np

from ml_services.api.face_detection.face_detection_retina import RetinaFaceSingleton
import threading

# lock_detected_image = threading.Lock()
lock_detected_image = QMutex()
import time

class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)

        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

# class ImagePreview(Widget):



class MLCamThread(QThread):
    get_recognition_signal = Signal(np.ndarray)
    change_pixmap_signal = Signal(np.ndarray)
    update_preview_face_signal = Signal()
    update_attendance_table_info = Signal()

    def __init__(self):
        super().__init__()
        self._run_flag = True
        self._run_ml = False
        self._preview_face = False
        self._show_table_info = False

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                if self._run_ml:
                    ori_img, faces, cv_img = self._do_ml_services(cv_img)
                    if self._preview_face:
                        self._do_preview_face(ori_img, faces)
                        pass

                    if self._show_table_info:
                        pass

                self.change_pixmap_signal.emit(cv_img)

        # shut down capture system
        cap.release()

    def set_run_ml(self, run_ml, ml_func=None):
        self._run_ml = run_ml
        self._do_ml_services = ml_func

    def set_preview_face(self, preview_face, preview_face_func=None):
        self._preview_face = preview_face
        self._do_preview_face = preview_face_func

    def setup_show_table_info(self, show_table_info, show_table_info_func=None):
        self._show_table_info = show_table_info
        self._do_show_table_info = show_table_info_func

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class RecognitionWidget(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setObjectName(u"cam_widget")
        self.setGeometry(parent.geometry())
        sizePolicy.setHeightForWidth(parent.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        
        self.display_width = 640
        self.display_height = 480

        self.image_label = QLabel(self)
        self.image_label.resize(self.display_width, self.display_height)

        self.view_thread = None
        self.capture_thread = None
        self.detected_image = []

        model_pack_name = 'buffalo_m'
        root = 'ml_services/data/model'
        self.face_detector = RetinaFaceSingleton(root, model_pack_name, providers=[ 'CPUExecutionProvider'])
        self.face_detector.prepare(ctx_id=0, det_size=(self.display_height, self.display_width))

        self.view_camera()

    def closeEvent(self, event):
        if self.capture_thread is not None:
            self.capture_thread.stop()
        if self.view_thread is not None:
            self.view_thread.stop()
        event.accept()

    def view_camera(self):
        if self.capture_thread is not None:
            self.capture_thread.stop()
        # create the video capture thread
        self.view_thread = MLCamThread()
        # connect its signal to the update_image slot
        self.view_thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.view_thread.start()

    def setup_run_ml_services(self):
        self._start_attendance = True
        # self.view_thread.get_recognition_signal.connect(self.recognize)
        self.view_thread.set_run_ml(self._start_attendance, self.recognize)

    def setup_preview_face(self, preview_layout):
        print('setup here')
        self._preview_face = True
        self.view_thread.set_preview_face(self._preview_face, self.show_preview_face)
        self.preview_layout = preview_layout
        self._list_pic_preview_layout = [None] * 5

        for i in range(5):
            self._list_pic_preview_layout[i] = QLabel(QWidget())
            self.preview_layout.addWidget(self._list_pic_preview_layout[i])
            print("append pic", i, self._list_pic_preview_layout[i])
    
    def setup_show_table_info(self, table_widget):
        self._show_table_info = True


    @Slot(np.ndarray, list)   
    def show_preview_face(self, cv_img, faces):
        if len(faces) > 0:
            print(faces[0].keys())
        if len(faces) > 5:
            faces.sort(descending=True, key=lambda x: x['det_score'])
            faces = faces[:5]

        for i, face in enumerate(faces):
            box = face.bbox.astype(np.int)
            print(box)
            x = max(box[0], 0)
            y = max(box[1], 0)
            w = box[2] - x
            h = box[3] - y

            cropped_img = cv_img[y:y+h, x:x+w]
            print(type(cropped_img))
            
            print("pic ", i)
            pic = self._list_pic_preview_layout[i]
            pixmap = self.convert_cv_qt(cropped_img)
            pic.setPixmap(pixmap)

            


        pass

    @Slot(np.ndarray)   
    def recognize(self, cv_img):
        """Updates the image_label with a new opencv image"""
        faces = self.face_detector.get(cv_img)
        rimg = self.face_detector.draw_on(cv_img, faces)
        return cv_img, faces, rimg

    @Slot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        # faces = self.face_detector.get(cv_img)
        # rimg = self.face_detector.draw_on(cv_img, faces)

        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)