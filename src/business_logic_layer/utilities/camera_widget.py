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


class CameraWidget(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setWindowTitle("Qt live label demo")
        # self.display_width = 640
        # self.display_height = 480
        # # create the label that holds the image
                # # create a text label
        # self.textLabel = QLabel('Webcam')

        # # create a vertical box layout and add the two labels
        # vbox = QVBoxLayout()
        # vbox.addWidget(self.image_label)
        # vbox.addWidget(self.textLabel)
        # # set the vbox layout as the widgets layout
        # self.setLayout(vbox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setObjectName(u"cam_widget")
        self.setGeometry(parent.geometry())
        sizePolicy.setHeightForWidth(parent.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        
        # self.display_width = parent.geometry().width()
        self.display_width = 640
        # self.display_height = parent.geometry().height()
        self.display_height = 480

        self.image_label = QLabel(self)
        self.image_label.resize(self.display_width, self.display_height)

        self.thread = None
        self.detected_image = []
        self.view_camera()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    def view_camera(self):
        if self.thread is not None:
            self.thread.stop()
        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    def capture_image(self):
        self.detected_image = []
        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.capture_face)
        # start the thread
        self.thread.start()

        print('thread started')

    def capture_face(self, cv_img):
        print("capture face")
        """Updates the image_label with a new opencv image"""
        model_pack_name = 'buffalo_m'
        root = 'ml_services/data/model'

        app = RetinaFaceSingleton(root, model_pack_name, providers=[ 'CPUExecutionProvider'])
        app.prepare(ctx_id=0, det_size=(self.display_height, self.display_width))
        faces = app.get(cv_img)
        rimg = app.draw_on(cv_img, faces)

        qt_img = self.convert_cv_qt(rimg)
        self.image_label.setPixmap(qt_img)

        global lock_detected_image

        # lock_detected_image.acquire()
        lock_detected_image.lock()
        print('lock 2')
        if len(self.detected_image) < 30:
            self.detected_image.append((cv_img, faces, rimg))
            QThread.sleep(0.1)
        print(len(self.detected_image))
        if len(self.detected_image) == 30:
            self.view_camera()
        # lock_detected_image.release()
        lock_detected_image.unlock()
        print('release 2')
        # 

    @Slot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        model_pack_name = 'buffalo_m'
        root = 'ml_services/data/model'

        app = RetinaFaceSingleton(root, model_pack_name, providers=['CPUExecutionProvider'])
        app.prepare(ctx_id=0, det_size=(self.display_height, self.display_width))
        faces = app.get(cv_img)
        rimg = app.draw_on(cv_img, faces)

        qt_img = self.convert_cv_qt(rimg)
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)