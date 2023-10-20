import numpy as np
import cv2 as cv

font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX 
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # insert a label in video
    cv.putText(gray,'Luciano',(100,50), font, 1,(255,0,0),2,cv.LINE_AA)
    
    # Display the resulting frame
    cv.imshow('frame', gray)

    if cv.waitKey(1) == ord('q'):
        for i in range(0,19):
            print(cap.get(i))
        break

cap.release()
cv.destroyAllWindows()