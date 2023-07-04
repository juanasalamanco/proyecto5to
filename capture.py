import cv2
#print(cv2.__version__)

vid = cv2.VideoCapture(0)
  
while(True):
      
    ret, frame = vid.read()
  
    cv2.imshow('frame', frame)
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
vid.release()
cv2.destroyAllWindows()
