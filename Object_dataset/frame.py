import cv2
import numpy as np

cap=cv2.VideoCapture('C:\\Users\Yashashvi\Documents\source_code\los_angeles.mp4')

while True:

 _, frame=cap.read()

 cv2.imshow('Frame', frame)
 cv2.waitKey(0)
