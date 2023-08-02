import threading
import cv2
import time
import numpy as np

# def set_interval(func, sec):
#     def func_wrapper():
#         set_interval(func, sec)
#         func()
#     t = threading.Timer(sec, func_wrapper)
#     t.start()
#     return t

# h = 0

# def video1():
#     vid = cv2.VideoCapture(1)
#     print("Running function")

#     while(not (cv2.waitKey(1) & 0xFF == ord('q'))):
#         ret, frame = vid.read()
#         cv2.imshow('frame', frame)
    
#     vid.release()
#     cv2.destroyAllWindows()

#     return

# t = set_interval(video1, 5)

cap = cv2.VideoCapture(1)
if (cap.isOpened()== False):
    print("Error opening video file")
  
while(cap.isOpened()):
    ret, frame = cap.read()
    print("hola")
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()