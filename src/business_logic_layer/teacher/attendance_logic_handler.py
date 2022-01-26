from PySide6 import QtGui
from PySide6.QtWidgets import QSizePolicy, QWidget, QApplication, QLabel, QVBoxLayout, QTableWidgetItem
from PySide6.QtGui import QPixmap
import sys
import cv2
from PySide6.QtCore import QRect, Signal, Slot, Qt, QThread, QMutex
import numpy as np

from ml_services.api.face_recognition.face_recognition_arcface import ArcFaceSingleton
from business_logic_layer.database_connector.mysql_connector import MySQLConnector
import threading

# lock_detected_image = threading.Lock()
lock_detected_image = QMutex()
from datetime import datetime

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
        self.face_detector = ArcFaceSingleton(root, model_pack_name, providers=[ 'CPUExecutionProvider'])
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
        self._setup_knn_model()
        self._setup_db_connection()
        self.attendance_mssv = {}
        self.view_thread.set_run_ml(self._start_attendance, self.recognize)

       

    def _setup_knn_model(self):
        import os
        from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
        data_dir = 'data/face'
        data = []
        label = []
        cnt = 0
        self.label_name = []
        for root, _, filenames in os.walk(data_dir):
            # print(root)

            if len(filenames) > 0:
                l_name = root.split(os.sep)[-1]
                # print(l_name)
                self.label_name.append(l_name)
                cnt += 1

                for filename in filenames:
                    img_path = os.path.join(root, filename)
                    img = cv2.imread(img_path)
                    faces = self.face_detector.get(img)
                    face = faces[0]

                    # print(face.keys())
                    emb = face['embedding']
                    data.append(emb)
                    label.append(cnt)

        data = np.array(data, dtype=np.float32)
        label = np.array(label)
        n_neighbor = 5
        self.matching_model = KNeighborsClassifier( n_neighbors=n_neighbor,
                                                metric='cosine',
                                                algorithm='brute',
                                                n_jobs=-1)
        self.matching_model.fit(data, label)

    def _setup_db_connection(self):
        self.db_connector = MySQLConnector()
        pass



    def setup_preview_face(self, preview_layout):
        print('setup here')
        self._preview_face = True
        self.view_thread.set_preview_face(self._preview_face, self.show_preview_face)
        self.preview_layout = preview_layout
        self._list_pic_preview_layout = [None] * 5

        for i in range(5):
            self._list_pic_preview_layout[i] = QLabel(self.preview_layout.parentWidget())
            self.preview_layout.addWidget(self._list_pic_preview_layout[i])
    
    def setup_show_table_info(self, table_widget):
        self._show_table_info = True
        self.table_widget = table_widget

    def insert_to_db(self, mssv):
        self.db_connector.insert_attendance(mssv)
        pass

    def insert_to_table_info(self, mssv):
        self.attendance_mssv[mssv] = 1

        student_info = self.db_connector.get_student_info(mssv)
        time = datetime.now()
        student_his = self.db_connector.get_history(mssv, time)

        student_name = student_info['name']
        student_email = student_info['email']
        time_attend = student_his['time_attend']
        mssv = str(mssv)

        rowPosition = self.table_widget.rowCount()
        self.table_widget.insertRow(rowPosition)
        self.table_widget.setItem(rowPosition , 0, QTableWidgetItem(mssv))
        self.table_widget.setItem(rowPosition , 1, QTableWidgetItem(student_name))
        self.table_widget.setItem(rowPosition , 2, QTableWidgetItem(student_email))
        self.table_widget.setItem(rowPosition , 3, QTableWidgetItem(time_attend))
        
        pass


    @Slot(np.ndarray, list)   
    def show_preview_face(self, cv_img, faces):
        # if len(faces) > 0:
            # print(faces[0].keys())
        if len(faces) > 5:
            faces.sort(reverse=True, key=lambda x: x['det_score'])
            faces = faces[:5]

        for i in range(5):
            self._list_pic_preview_layout[i].clear()

        for i, face in enumerate(faces):
            box = face.bbox.astype(np.int)
            # print(box)
            x = max(box[0], 0)
            y = max(box[1], 0)
            w = box[2] - x
            h = box[3] - y

            cropped_img = cv_img[y:y+h, x:x+w]
            
            pic = self._list_pic_preview_layout[i]

            size = (128, 128)
            cropped_img = cv2.resize(cropped_img, size, interpolation=cv2.INTER_CUBIC)

            pixmap = self.convert_cv_qt(cropped_img, keep_shape=True)
            pic.setPixmap(pixmap)

            


        pass

    @Slot(np.ndarray)   
    def recognize(self, cv_img):
        """Updates the image_label with a new opencv image"""
        faces = self.face_detector.get(cv_img)

        for face in faces:
            emb = [face['embedding']]
            emb = np.array(emb, dtype=np.float32)
            label = self.matching_model.predict(emb)[0]
            l_name = self.label_name[label-1]
            mssv = int(l_name)

            if mssv not in self.attendance_mssv:
                self.insert_to_db(mssv)
                self.insert_to_table_info(mssv)
            # print(label, l_name)


        rimg = self.face_detector.draw_on(cv_img, faces)
        return cv_img, faces, rimg

    @Slot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        # faces = self.face_detector.get(cv_img)
        # rimg = self.face_detector.draw_on(cv_img, faces)

        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img, keep_shape=False):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        if keep_shape:
            p = convert_to_Qt_format.scaled(w, h, Qt.KeepAspectRatio)
        else:
            p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)