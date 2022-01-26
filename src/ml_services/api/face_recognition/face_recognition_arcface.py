import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image
from datetime import datetime
import os
from ..utilities.singleton_meta import SingletonMeta


class ArcFaceSingleton(metaclass=SingletonMeta):

    def __init__(self, root: str, model_name : str, *args, **kwargs) -> None:
        self.app = FaceAnalysis(root = root, name = model_name, *args, allowed_modules=['detection','recognition'], **kwargs)
        
    def get(self, img, max_num=0):
        return self.app.get(img, max_num)

    def draw_on(self, img, faces):
        import cv2
        dimg = img.copy()
        for i in range(len(faces)):
            face = faces[i]
            box = face.bbox.astype(np.int)
            color = (0, 0, 255)
            cv2.rectangle(dimg, (box[0], box[1]), (box[2], box[3]), color, 2)
            if face.kps is not None:
                kps = face.kps.astype(np.int)
                #print(landmark.shape)
                for l in range(kps.shape[0]):
                    color = (0, 0, 255)
                    if l == 0 or l == 3:
                        color = (0, 255, 0)
                    cv2.circle(dimg, (kps[l][0], kps[l][1]), 1, color,
                               2)
            if face.gender is not None and face.age is not None:
                cv2.putText(dimg,'%s,%d'%(face.sex,face.age), (box[0]-1, box[1]-4),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),1)

            #for key, value in face.items():
            #    if key.startswith('landmark_3d'):
            #        print(key, value.shape)
            #        print(value[0:10,:])
            #        lmk = np.round(value).astype(np.int)
            #        for l in range(lmk.shape[0]):
            #            color = (255, 0, 0)
            #            cv2.circle(dimg, (lmk[l][0], lmk[l][1]), 1, color,
            #                       2)
        return dimg

    def prepare(self, ctx_id, det_thresh=0.5, det_size=(640, 640)):
        return self.app.prepare(ctx_id, det_thresh, det_size)