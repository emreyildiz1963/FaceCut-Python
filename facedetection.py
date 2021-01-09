import cv2
import os
import numpy as np

haarcascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')


def facedetect(img_path):
    
    GR_dict={1:(0,0,255),0:(0,255,0)}
    results={1:'Maskesiz',0:'Maskeli'}

    rect_size = 4

    shapez=150



    im = cv2.imread(img_path)
    im=cv2.flip(im,1,1)
    rerect_size = cv2.resize(im, (im.shape[1] // rect_size, im.shape[0] // rect_size))
    faces = haarcascade.detectMultiScale(rerect_size)
    kontrol = False
    for f in faces:
        (x, y, w, h) = [v * rect_size for v in f] 

        face_img = im[y:y+h, x:x+w]
        rerect_sized=cv2.resize(face_img,(shapez,shapez))
        normalized=rerect_sized/255.0
        reshaped=np.reshape(normalized,(1,shapez,shapez,3))
        reshaped = np.vstack([reshaped])
        kontrol = True
    if kontrol:
        return face_img
    pass


