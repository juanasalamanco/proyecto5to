import cv2

def videoStream():
  vid = cv2.VideoCapture(0)
  while True:
    ret, frame = vid.read()
    if ret == True:
      cv2.imshow("capturando...", frame)
      key = cv2.waitKey(1)
      if key == ord("q"):
        break
  
  vid.release()
  cv2.destroyAllWindows()
  return ret, frame

# def video_frame(label, bbox):
#   data = eval_js('stream_frame("{}", "{}")'.format(label, bbox))
#   return data

#------------------------------------------------------------------
vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()