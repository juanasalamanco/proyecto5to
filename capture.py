import cv2
print(cv2.__version__)

vid = cv2.VideoCapture(0)

while True:
    
    ret, frame = vid.read()

    if ret == True:
        cv2.imshow("hola", frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
  
vid.release()
cv2.destroyAllWindows()
