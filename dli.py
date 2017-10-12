import os
import dlib
import glob
import cv2
import numpy as np
predictor_path = "./shape_predictor_68_face_landmarks.dat"
f= "azc.jpg"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)


img = cv2.imread(f)

dets = detector(img, 1)
o=[]
for k, d in enumerate(dets):
    shape = predictor(img, d)
    for i in range(0, 68):
        x = shape.part(i).x
        y = shape.part(i).y
        o.append(x)
        o.append(y)
    print o

        
kp=np.array(o)
np.save('aca',kp)     
