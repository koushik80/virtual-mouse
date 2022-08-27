from asyncore import read
import cv2


cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    cv2.imshow('Eye-controlled-mouse', frame)
    cv2.waitKey(1)
