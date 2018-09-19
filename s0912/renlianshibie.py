#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'stdu.tslhw'
import cv2
import numpy as np

pathj=r'C:\Users\chenb\PycharmProjects\12306\venv\src\s0912\haarcascade_eye.xml'
pathf=r'C:\Users\chenb\PycharmProjects\12306\venv\src\s0912\haarcascade_frontalface_default.xml'
eye_xml = cv2.CascadeClassifier(pathj)
face_xml = cv2.CascadeClassifier(pathf)
#eye_xml = cv2.CascadeClassifier(r"C:\Users\chenb\PycharmProjects\12306\venv\src\s0912\defualt.xml")
#face_xml = cv2.CascadeClassifier(r"C:\Users\chenb\PycharmProjects\12306\venv\src\s0912\VID5.xml")

if eye_xml.empty():
    pass

# load jpg
img = cv2.imread('face.jpg')
cv2.imshow('src',img)

# haar gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detect face
faces = face_xml.detectMultiScale(gray, 1.3, 5)  # 灰度图片数据，1.3为缩放数据，5是最小像素点
print('faces')
print('face=',len(faces))
# draw

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_face = gray[y:y+h,x:x+w]
    roi_color = img[y:y+h,x:x+w]
    eyes = eye_xml.detectMultiScale(roi_face)
    print('eye=',len(eyes))
    for (e_x,e_y,e_w,e_h) in eyes:
        cv2.rectangle(roi_color, (e_x, e_y), (e_x + e_w, e_y + e_h), (0, 255, 0), 2)
cv2.imshow('dst',img)
cv2.waitKey(0)




