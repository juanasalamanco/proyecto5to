import threading
import cv2
import time

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

h = 0

def video1():
    vid = cv2.VideoCapture(0)
    print("Running function")

    while(not (cv2.waitKey(1) & 0xFF == ord('q'))):
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
    
    vid.release()
    cv2.destroyAllWindows()

    return

t = set_interval(video1, 5)

vid = cv2.VideoCapture(0)
while(True):
  print("hola")
  ret, frame = vid.read()
  cv2.imshow('frame', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
vid.release()
cv2.destroyAllWindows()