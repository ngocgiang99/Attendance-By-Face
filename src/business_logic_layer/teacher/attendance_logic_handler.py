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
        self.view_thread = VideoThread()
        # connect its signal to the update_image slot
        self.view_thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.view_thread.start()

    def setup_run_ml_services(self):
        self._start_attendance = True

    def setup_preview_face(self, preview_layout):
        self._preview_face = True
    
    def setup_show_table_info(self, table_widget):
        self._show_table_info = True


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